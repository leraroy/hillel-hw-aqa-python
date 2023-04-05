"""
Пользователь вводит высоту и ширину прямоугольника (целые числа) и символ.

Вывести прямоугольник составленный из введенного символа заданного размера

> Enter height of rectangular: 3
> Enter width of rectangular: 6
> Enter symbol to build rectangular with: ^
^^^^^^
^^^^^^
^^^^^^
"""

height = int(input("Enter height of rectangular: "))
width = int(input("Enter width of rectangular: "))
symbol = input("Enter symbol to build rectangular with: ")

print((symbol*width+"\n")*height)