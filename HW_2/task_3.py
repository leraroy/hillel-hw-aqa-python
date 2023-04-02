"""
Запросить у пользователя два целых числа.

Вывести на одной строке выражение их суммы, на второй выражение для произведения:

Enter a: 3
Enter b: 5
3 + 5 = 8
3 * 5 = 15
"""

# version 1
a = int(input("Enter a: "))
b = int(input("Enter b: "))

print(f"{a} + {b} = {a+b}")
print(f"{a} * {b} = {a*b}")

# version 2

a = int(input("Enter a: "))
b = int(input("Enter b: "))

print(str(a) + " + " + str(b) + " = " + str(a+b))
print(str(a) + " * " + str(b) + " = " + str(a*b))