"""
Тестирование класса Pixel

Реализован класс Pixel. Написать к нему тесты, найти и исправить дефекты. Протектед методы явно не тестировать (только паблик и операторы).
Дефекты, коротко описать в тестах, которые их находят в маркере xfail(reason="Defect description")

Описние класса:
Конструктор должен принимать три аргумента - красная, зеленая и голубая компоненты пикселя.
Это целые числа в диапазоне [0, 255] (включительно).
При попытке создать объект с компонентами не из этого диапазова должно выбрасываться исключение ValueError
Компоненты должны быть приватными полями. Для их получения должны быть написаны проперти.

Класс Pixel должен реализовать перегрузку операторов +, - * (слева и справа), /, == и переопределять методы __str__ и __repr__ (возвращая строку с вызовом конструктора).

Оператор +(-) позволяет сложить (вычесть) два объекта класса Pixel.
В результате сложения (вычитания) должен возвращаться новый объект класса Pixel с компонентами равными сумме (разности) исходных объектов.

Оператор * (/) позволяет умножить (разделить) объект класса Pixel на число типа int или float больше 0.
В результате умножения должен возвращаться новый объекта класса Pixel с компонентами равными произведению (частному) компонент исходного объекта на число.
При попытке умножить (разделить) не на числа типа int или float должно выбрасываться исключение TypeError.
При попытке умножить (разделить) на число ноль или меньше нуля должно выбрасываться исключение ValueError.
Если при умножении (делении) компоненты на число получилось дробное число, дробную часть надо отброcить.

Если в результате применения операторов, какая-то компонента будет меньше 0, ее необходимо установить в 0.
Если в результате применения операторов, какая-то компонента будет больше 255, ее необходимо установить в 255.

Два объекта типа Pixel с равными компонентами считаются равными

Метод __str__ должен возвращать строку следующего вида:
Pixel object
\tRed: 14
\tGreen: 128
\tBlue: 236

Метод __repr__ должен должен возвращать строку с вызовом конструктора

У класса Pixel должен быть метод get_pixel_near(area: int), который вернет случайный пиксель, компоненты которого находятся не дальше +/- area
"""

from __future__ import annotations

import random


class Pixel:

    # add raise TypeError for components not int
    def __init__(self, r, g, b):
        if not all(isinstance(component, (int, float)) for component in [r, g, b]):
            raise TypeError("Pixel components must be integers")
        if len(list(filter(lambda component: 0 <= component <= 255, [r, g, b]))) != 3:
            raise ValueError(f"One of the Pixel components ({r}, {g}, {b}) is not in range of [0, 255]")

        self.__r = r
        self.__g = g
        self.__b = b

    @property
    def r(self):
        return self.__r

    @property
    def g(self):
        return self.__g

    @property
    def b(self):
        return self.__b

    def __add__(self, other: Pixel):
        new_r = Pixel._convert_to_byte(self.__r + other.__r)
        new_g = Pixel._convert_to_byte(self.__g + other.__g)
        new_b = Pixel._convert_to_byte(self.__b + other.__b)
        return Pixel(new_r, new_g, new_b)

    def __sub__(self, other: Pixel):
        new_r = Pixel._convert_to_byte(self.__r - other.__r)
        new_g = Pixel._convert_to_byte(self.__g - other.__g)
        new_b = Pixel._convert_to_byte(self.__b - other.__b)
        return Pixel(new_r, new_g, new_b)

    # If, when multiplying (dividing) a component by a number, a
    # fractional number is obtained, the fractional part must be discarded.
    # add int
    def __pixel_multiplication(self, multiplicator):
        Pixel._check_if_value_is_int_or_float(multiplicator)
        Pixel._check_if_value_greater_than_zero(multiplicator)
        new_r = Pixel._convert_to_byte(int(self.__r * multiplicator))
        new_g = Pixel._convert_to_byte(int(self.__g * multiplicator))
        new_b = Pixel._convert_to_byte(int(self.__b * multiplicator))
        return Pixel(new_r, new_g, new_b)

    def __mul__(self, multiplicator):
        return self.__pixel_multiplication(multiplicator)

    # this code is the same as __mul__
    def __rmul__(self, multiplicator):
        return self.__pixel_multiplication(multiplicator)

    # Divider should be greater than 0
    def __truediv__(self, multiplicator):
        Pixel._check_if_value_is_int_or_float(multiplicator)
        Pixel._check_if_value_greater_than_zero(multiplicator)
        new_r = Pixel._convert_to_byte(int(self.__r / multiplicator))
        new_g = Pixel._convert_to_byte(int(self.__g / multiplicator))
        new_b = Pixel._convert_to_byte(int(self.__b / multiplicator))
        return Pixel(new_r, new_g, new_b)

    def __eq__(self, other: Pixel):
        return self.__r == other.__r and self.__g == other.__g and self.__b == other.__b

    def __str__(self):
        return f"Pixel object\n\tRed: {self.__r}\n\tGreen: {self.__g}\n\tBlue: {self.__b}\n"

    def __repr__(self):
        return f"Pixel({self.__r}, {self.__g}, {self.__b})"

    # add self._convert_to_byte for Pixel components
    # Если в результате применения операторов, какая-то компонента будет меньше 0, ее необходимо установить в 0.
    # Если в результате применения операторов, какая-то компонента будет больше 255, ее необходимо установить в 255.
    # add self._check_if_value_is_int_or_float
    def get_pixel_near(self, area):
        self._check_if_value_is_int_or_float(area)
        neighbourhood = -area + 2 * area * random.random()
        return Pixel(self._convert_to_byte(self.r + neighbourhood),
                     self._convert_to_byte(self.b + neighbourhood),
                     self._convert_to_byte(self.g + neighbourhood))

    @staticmethod
    def _check_if_value_is_int_or_float(n):
        if not isinstance(n, (int, float)):
            raise TypeError("Pixel could be multiplied only by int or float")

    # add ZeroDivisionError for value 0
    @staticmethod
    def _check_if_value_greater_than_zero(n):
        if n == 0:
            raise ZeroDivisionError("Multiplicator should be greater than 0")
        if n < 0:
            raise ValueError("Multiplicator should be greater than 0")

    @staticmethod
    def _convert_to_byte(n: int):
        if n < 0:
            return 0.0
        elif n > 255:
            return 255
        else:
            return n
