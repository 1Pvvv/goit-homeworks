# Docker-команда FROM указывает базовый образ контейнера
# Наш базовый образ - это Linux с предустановленным python-3.11
FROM python:3.11

# Установим переменную окружения
ENV PYTHONUNBUFFERED 1

# Установим рабочую директорию внутри контейнера
WORKDIR /app

# Скопируем остальные файлы в рабочую директорию контейнера
COPY pyproject.toml poetry.lock /app/

# Установим poetry
RUN pip install poetry && poetry config virtualenvs.create false

# Установим зависимости проекта
#RUN poetry install

# Скопируем остальные файлы проекта в рабочую директорию
COPY . /app/

# Переходим в рабочую директорию внутри контейнера
WORKDIR /app/2-2-poetry

# Запустим наше приложение
CMD ["python", "__init__.py"]