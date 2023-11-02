FROM python:3.11

RUN pip install poetry

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-root

COPY . .

WORKDIR /app/2_2_poetry

CMD ["python3", "__init__.py"]
