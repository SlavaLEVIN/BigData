# ДЗ №3. Spark Streaming

[Условие](https://github.com/SergUSProject/BigDataProc_HomeWorks/blob/main/spark/docs/BigData_HW3.md).

Поток данных: Telegram → Kafka → Spark Streaming. Пока подготовлены только ноутбуки; сборщик и Kafka не настроены.

Пока оставлены заготовки, решения не добавлены.

## Оглавление

1. [Количество сообщений](%D0%97%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5%201/01_messages.ipynb)
2. [Частоты собственных имён](%D0%97%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5%202/01_names.ipynb)
3. [Собственные имена по каналам](%D0%97%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5%203/01_channels.ipynb)

## Среда

- Python 3.11
- Java 17
- PySpark 3.5.7
- VS Code с расширениями Python и Jupyter; также можно использовать JupyterLab.

## Установка на macOS

Из корня репозитория, при установленных Homebrew и uv:

```sh
cd DZ_3
brew install openjdk@17
export JAVA_HOME="$(brew --prefix openjdk@17)/libexec/openjdk.jdk/Contents/Home"
export PATH="$JAVA_HOME/bin:$PATH"
uv venv --python 3.11 .venv
source .venv/bin/activate
uv pip install -r requirements.txt
```

В VS Code выбрать ядро ноутбука: `Python Environments → DZ_3/.venv/bin/python`. Для работы в браузере запустить `python -m jupyterlab` из активированной среды.

При следующем запуске достаточно активировать существующую `.venv` и выбрать её в ноутбуке. Java должна быть доступна ядру VS Code через `JAVA_HOME` или `PATH`.

## Данные

Сообщения поступают из Telegram. ID каналов приведены в исходном условии. Нужны собственные `api_id` и `api_hash`, а также запущенная Kafka.

В условии указаны `telethon==1.24.0` и `kafka-python==2.0.2`; они добавлены в requirements.txt. Пароли, API hash и файлы сессий в репозитории не хранятся.

В задании №3 вместо условия стоит `TODO`. Его реализацию пока не начинаем.

Результаты расчётов сохраняются в `output/` рядом с ноутбуком и не добавляются в Git.
