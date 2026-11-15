# ДЗ №2. Анализ поездок, DataFrame API

[Условие](https://github.com/SergUSProject/BigDataProc_HomeWorks/blob/main/spark/docs/BigData_HW2.md).

Обработка данных выполняется через Spark DataFrame API.

Пока оставлены заготовки, решения не добавлены.

## Оглавление

1. [Станции и городские зоны](%D0%97%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5%201/01_stations.ipynb)
2. [Расстояния поездок](%D0%97%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5%202/01_distances.ipynb)
3. [Активность по времени](%D0%97%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5%203/01_time.ipynb)

## Среда

- Python 3.11
- Java 17
- PySpark 3.5.7
- VS Code с расширениями Python и Jupyter; также можно использовать JupyterLab.

## Установка на macOS

Из корня репозитория, при установленных Homebrew и uv:

```sh
cd DZ_2
brew install openjdk@17
export JAVA_HOME="$(brew --prefix openjdk@17)/libexec/openjdk.jdk/Contents/Home"
export PATH="$JAVA_HOME/bin:$PATH"
uv venv --python 3.11 .venv
source .venv/bin/activate
uv pip install -r requirements.txt
```

В VS Code выбрать ядро ноутбука: `Python Environments → DZ_2/.venv/bin/python`. Для работы в браузере запустить `python -m jupyterlab` из активированной среды.

При следующем запуске достаточно активировать существующую `.venv` и выбрать её в ноутбуке. Java должна быть доступна ядру VS Code через `JAVA_HOME` или `PATH`.

## Данные

Для работы используются файлы за апрель 2026 года, полученные от преподавателя. Они лежат непосредственно в `DZ_2/`:

- `202604-citibike-tripdata-part1.csv`;
- `202604-citibike-tripdata-part2.csv`;
- `202604-citibike-tripdata-part3.csv`;
- `202604-citibike-tripdata-part4.csv`;
- `JC-202604-citibike-tripdata.csv`.

CSV исключены из Git. После клонирования их нужно скопировать в эту папку. В исходном условии указан 2019 год, здесь используем набор преподавателя.

[GeoJSON городских зон](https://data.cityofnewyork.us/api/geospatial/d3c5-ddgc?method=export&format=GeoJSON) нужно сохранить в `data/`. Библиотеки для карт добавим при реализации.

Результаты расчётов сохраняются в `output/` рядом с ноутбуком и не добавляются в Git.
