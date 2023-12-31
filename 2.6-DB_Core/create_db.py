import sqlite3


def create_db():
    # читаем файл со скриптом для создания БД
    with open('./queries/create_university.sql', 'r') as f:
        sql = f.read()

    # создаем соединение с БД (если файла с БД нет, он будет создан)
    with sqlite3.connect('university.db') as con:
        cur = con.cursor()
        # выполняем скрипт из файла, который создаст таблицы в БД
        cur.executescript(sql)


create_db()
