"""
Напишите реализацию функции factorize, которая принимает список чисел и возвращает список чисел, на которые числа из входного списка делятся без остатка.

Реализуйте синхронную версию и измерьте время выполнения.

Потом улучшите производительность вашей функции, реализовав использование нескольких ядер процессора для параллельных вычислений, и замерьте время выполнения опять.
Для определения количества ядер на машине используйте функцию cpu_count() из пакета multiprocessing

Для проверки правильности работы алгоритма самой функции можете воспользоваться тестом:
"""

# MULTIPROCESSING
import logging

from time import time
from typing import List
from multiprocessing import cpu_count, Pool, freeze_support, current_process


logger = logging.getLogger()
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)
timer = time()

def check_modulo(x: int, y: int) -> bool:
    if x % y == 0:
        return True
    return False

def factorize(num: int) -> List[int]:
    logger.debug(f"pid: {current_process().pid}; num to calc = {num}")
    return [x for x in range(1, num+1) if check_modulo(num, x)]


if __name__ == '__main__':
    data = (128, 255, 99999, 10651060)

    freeze_support()
    with Pool(processes=cpu_count()) as pool:
        a, b, c, d = pool.map(factorize, data)

    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]

    logger.debug(f'Multiprocessing: Done in {time()-timer} sec')
