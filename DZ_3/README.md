# ДЗ №3. Spark Streaming

Реализованы задания 1–3. Для проверки на настоящих сообщениях нужны ключи Telegram.

## Оглавление

[Задания 1–3](01_streaming.ipynb)

## Среда

Python 3.11, Java 17, PySpark 3.5.7 и Docker Desktop.
Используем `telethon==1.46.0`: при входе на версии 1.24.0 Telegram возвращает `UPDATE_APP_TO_LOGIN`.

## Запуск

Запусти Docker Desktop. Из папки `DZ_3` выполни:

```bash
uv venv --python 3.11 .venv
uv pip install --python .venv/bin/python -r requirements.txt
docker compose up -d
docker compose exec kafka /opt/kafka/bin/kafka-topics.sh --bootstrap-server localhost:9092 --create --if-not-exists --topic telegram_messages --partitions 1 --replication-factor 1
```

При первом запуске заполни `.env` по образцу `.env.example` и выполни `.venv/bin/python telegram_producer.py`. После входа и подключения каналов останови сборщик через Ctrl+C. Сессия сохранится.

В VS Code выбери ядро из `.venv` и нажми **Run All** в тетради. Последняя ячейка сама запустит сборщик и покажет результаты. Минутные файлы появятся в `output`.
