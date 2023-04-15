"""
Есть список состоящий из целых чисел. Создать три списка:

- в первый список добавить числа, которые делятся только на 3

- во второй список добавить числа, которые делятся только на 5

- в третий список добавить числа, которые делятся и на 3, и на 5


[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]  # Input list
[3, 6, 9, 12]  # elements divided by 3
[5, 10]  # elements divided by 5
[0, 15]  # elements divided by 3 and by 5
"""

input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
divided_by_3 = []
divided_by_5 = []
divided_by_both = []
print(f"{input_list} - Input list")

for i in input_list:
    if i % 3 == 0 and not i % 5 == 0:
        divided_by_3.append(i)
    if i % 5 == 0 and not i % 3 == 0:
        divided_by_5.append(i)
    if i % 3 == 0 and i % 5 == 0:
        divided_by_both.append(i)
print(f"{divided_by_3} - elements divided by 3")
print(f"{divided_by_5} - elements divided by 5")
print(f"{divided_by_both} - elements divided by 3 and by 5")


