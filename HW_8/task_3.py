"""
Написать генераторную функцию, которая принимает два параметра m, n.

Генератор должен возвращать числа от 1 до n (включительно),
затем числа от 1 до n в квадрате, и так до степени m (включительно)

for i in generator(3, 4):
    print(i)
# 1, 2, 3, 4, 1, 4, 9, 16, 1, 8, 27, 64
"""
import math


def generator(m, n):
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            yield int(math.pow(j, i))


for i in generator(3, 4):
    print(i, end=' ')
