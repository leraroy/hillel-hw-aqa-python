"""
Написать функцию, которая возвращает слуайную строку заданной длины.

Строка должна состоять из больших и маленьких латинских
 букв и цифр.

(снижать за это оценку не буду, но лучше постараться сделать
 так, чтобы символы попадали в строку равномерно)

def get_random_string(length: int) -> str:
    pass

Ограничения:
- Не использовать модуль string
- Не создавать руками список ['a', 'b', 'c', ..., 'X', 'Y', 'Z', 0, 1, ..., 8, 9]
"""
import random


def get_random_string(length: int) -> str:
    lower_case = [chr(i) for i in range(97, 123)]
    upper_case = [chr(i) for i in range(65, 91)]
    numbers = [chr(i) for i in range(48, 58)]
    return ''.join(random.choices((upper_case + lower_case + numbers), k=length))


for i in range(5):
    print(get_random_string(5))
