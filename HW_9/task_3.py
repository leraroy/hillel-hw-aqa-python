"""
Занятия проходят по понедельникам и четвергам в 19:15

Первое занятие произошло 27.03.2023.

Вывести список всех занятий в таком формате (номера
лекций выровнены по правому краю):


Lecture  1: 27 Mar 2023 19:15
Lecture  2: 30 Mar 2023 19:15
Lecture  3: 03 Apr 2023 19:15
...
Lecture  9: 24 Apr 2023 19:15
Lecture 10: 27 Apr 2023 19:15
...
Lecture 32: 13 Jul 2023 19:15
"""

from datetime import *


def lessons():
    start_date = datetime(2023, 3, 27, 19, 15)
    monday = start_date + timedelta(days=0 - start_date.weekday())
    thuesday = start_date + timedelta(days=3 - start_date.weekday())
    count = 1
    while count <= 32:
        yield monday
        count += 1
        yield thuesday
        count += 1
        monday += timedelta(days=7)
        thuesday += timedelta(days=7)


for item, value in enumerate(lessons()):
    print(f"Lecture {(item + 1):>2}: {(value.strftime('%d %b %Y %H:%M')):>10}")
