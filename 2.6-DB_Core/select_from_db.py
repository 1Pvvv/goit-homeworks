import sys
import sqlite3
from pprint import pprint


def select_from_db(query_number: int) -> list:
    # читаем файл со скриптом для выборки из БД
    try:
        with open(f'./queries/puery_{query_number}.sql', 'r') as f:
            sql = f.read()
    except FileNotFoundError:
        return 'Wrong query number'

    # создаем соединение с БД (если файла с БД нет, он будет создан)
    with sqlite3.connect('university.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


query_number = int(sys.argv[1])
pprint(select_from_db(query_number))
