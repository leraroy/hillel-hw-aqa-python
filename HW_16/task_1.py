"""
Написать класс Timer для измерения времени выполнения кода.
Прошедшее время должен возвращать в аттрибуте elapsed_time.
Класс должен применяться как контекстный менеджер.
У класса должен быть метод reset
Если между использованием контекстного менеджера
вызывался метод reset, прошедшее время должно считаться обнулятся.

Если метод reset не вызывался, в elapsed_time должно
быть сохранено время выполнения всех фрагментов кода
обернутых контекстным менеджером.

class Timer:
    pass


Пример использования:

with Timer() as t:
    time.sleep(1)
print(t.elapsed_time)  # ~1 second
time.sleep(1)
with t:
    time.sleep(2)
print(t.elapsed_time)  # ~3 seconds

with Timer() as t2:
    time.sleep(1)
print(t2.elapsed_time)  # ~1 second
t2.reset()
with t2:
    time.sleep(2)
print(t2.elapsed_time)  # ~2 seconds
"""

import time


class Timer:

    def __init__(self):
        self.elapsed_time = 0

    def __enter__(self):
        self.start = time.time()
        return self

    def reset(self):
        self.elapsed_time = 0

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.time()
        self.elapsed_time += self.end - self.start


with Timer() as t:
    time.sleep(1)
print(t.elapsed_time)  # ~1 second
time.sleep(1)
with t:
    time.sleep(2)
print(t.elapsed_time)  # ~3 seconds

with Timer() as t2:
    time.sleep(1)
print(t2.elapsed_time)  # ~1 second
t2.reset()
with t2:
    time.sleep(2)
print(t2.elapsed_time)  # ~2 seconds
