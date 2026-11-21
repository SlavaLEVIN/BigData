# ДЗ №4. Рекомендательные системы, MLlib

[Условие](https://github.com/SergUSProject/BigDataProc_HomeWorks/blob/main/spark/docs/BigData_HW4.md).

Задания выполняются сначала на малом, затем на полном MovieLens. Используется DataFrame API; для задания №2 допускается другой API. Варианты определяются по фамилии кодом из условия.

В задании 1 для фамилии Лёвин получен вариант 3 (Thriller, Sci-Fi, Adventure). Таблицы малого и полного набора находятся в тетради.

В задании 2 получен вариант 1. Сходство пользователей вычисляется по обучающим оценкам с учётом жанров фильмов. В тетради приведён RMSE двух прогнозов на одном и том же тестовом наборе.

## Оглавление

1. [Анализ MovieLens](%D0%97%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5%201/01_analysis.ipynb)
2. [Коллаборативная фильтрация](%D0%97%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5%202/01_collaborative.ipynb)
3. [Факторизация матрицы, ALS](%D0%97%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5%203/01_als.ipynb)

## Среда

- Python 3.11
- Java 17
- PySpark 3.5.7
- VS Code с расширениями Python и Jupyter; также можно использовать JupyterLab.

## Установка на macOS

Из корня репозитория, при установленных Homebrew и uv:

```sh
cd DZ_4
brew install openjdk@17
export JAVA_HOME="$(brew --prefix openjdk@17)/libexec/openjdk.jdk/Contents/Home"
export PATH="$JAVA_HOME/bin:$PATH"
uv venv --python 3.11 .venv
source .venv/bin/activate
uv pip install -r requirements.txt
```

В VS Code выбрать ядро ноутбука: `Python Environments → DZ_4/.venv/bin/python`. Для работы в браузере запустить `python -m jupyterlab` из активированной среды.

При следующем запуске достаточно активировать существующую `.venv` и выбрать её в ноутбуке. Java должна быть доступна ядру VS Code через `JAVA_HOME` или `PATH`.

## Данные

- [MovieLens ml-latest-small](https://files.grouplens.org/datasets/movielens/ml-latest-small.zip).
- [MovieLens ml-latest](https://files.grouplens.org/datasets/movielens/ml-latest.zip).

Обе папки с данными лежат прямо в `DZ_4/`. Одна копия каждого набора используется во всех трёх заданиях. Файлы данных исключены из Git.

В задании 1 используются `movies.csv` и `ratings.csv`. В VS Code запускайте ячейки по порядку из папки тетради.
