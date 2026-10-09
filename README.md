Скрипт качает файл по ссылке десять раз подряд каждый раз ждёт ответ и в конце пишет среднее время сколько всего скачалось и скорость в МБ с Нужен обычный Python 3 ничего ставить не надо

Запуск из этой папки

```
python speed_test.py "https://mirror.yandex.ru/ubuntu/pool/universe/c/chromium-browser/chromium-browser-l10n_34.0.1847.116-0ubuntu2_all.deb"
```

В кавычки можно подставить любой URL Имеет смысл брать что-то на пару мегабайт иначе увидишь в основном пинг а не скорость канала Нормальные варианты из РФ один и тот же пакет Ubuntu около 3 МБ с зеркала Яндекса и с Selectel

https://mirror.yandex.ru/ubuntu/pool/universe/c/chromium-browser/chromium-browser-l10n_34.0.1847.116-0ubuntu2_all.deb

https://mirror.selectel.ru/ubuntu/pool/universe/c/chromium-browser/chromium-browser-l10n_34.0.1847.116-0ubuntu2_all.deb

Картинки тоже ок если просто проверить что скрипт живой но они мелкие Хабр https://assets.habr.com/habr-web/release_2.352.4/client/img/vk/server-mobile.webp РИА https://cdnn21.imgria.ru/images/07ea/09/17/2118562452_0:0:2158:2157_925x0_80_0_0_f0676062553bee8960cf1ebf10941cc5.jpg

В консоли сначала десять строк по каждому запросу потом среднее время суммарный объём и скорость весь объём делим на суммарное время Если сервер ответил ошибкой на этом всё скрипт пишет код и выходит Wikimedia например после нескольких качаний подряд иногда отдаёт 429
