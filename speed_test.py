#!/usr/bin/env python3

import argparse
import sys
import time
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

MB = 1_000_000
RUNS = 10
CHUNK = 64 * 1024
TIMEOUT = 60

# иначе часть CDN отдаёт 403 на дефолтный urllib
UserAgent = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/129.0.0.0 Safari/537.36"
)


def fetch(url: str) -> tuple[int, float]:
    req = Request(
        url,
        headers={
            "User-Agent": UserAgent,
            "Accept": "*/*",
            "Cache-Control": "no-cache",
            "Pragma": "no-cache",
        },
    )

    started = time.perf_counter()
    total = 0
    with urlopen(req, timeout=TIMEOUT) as resp:
        while True:
            chunk = resp.read(CHUNK)
            if not chunk:
                break
            total += len(chunk)

    return total, time.perf_counter() - started


def mb(n: int) -> str:
    return f"{n / MB:.3f} МБ"


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Последовательный замер скорости по URL (10 GET).",
    )
    parser.add_argument("url", help="адрес файла, лучше что-то тяжёлое")
    args = parser.parse_args()

    times = []
    sizes = []

    print(f"GET {args.url}")
    print(f"{RUNS} запросов подряд\n")

    for i in range(1, RUNS + 1):
        try:
            size, elapsed = fetch(args.url)
        except HTTPError as exc:
            sys.exit(f"[{i}/{RUNS}] HTTP {exc.code} {exc.reason}")
        except URLError as exc:
            sys.exit(f"[{i}/{RUNS}] {exc.reason}")
        except TimeoutError:
            sys.exit(f"[{i}/{RUNS}] timeout")

        times.append(elapsed)
        sizes.append(size)
        print(f"[{i:>2}/{RUNS}]  {elapsed:7.3f} с   {mb(size)}")

    total_time = sum(times)
    total_bytes = sum(sizes)
    avg = total_time / len(times)
    speed = (total_bytes / MB) / total_time if total_time else 0.0

    print()
    print(f"среднее время   {avg:.3f} с")
    print(f"скачано         {mb(total_bytes)}  ({total_bytes} байт)")
    print(f"скорость        {speed:.3f} МБ/с")


if __name__ == "__main__":
    main()
