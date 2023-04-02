"""
Создать список из трех стран.

Создать словарь из трех пар ключ-значение. Ключом
должна быть строка с названием страны из первого списка,
значением строка со столицей.

Вывести каждую пару на отдельной строке, разделить
ключ-значение двоеточием и пробелом:

Ukraine: Kyiv
Spain: Madrid
Italy: Rome
"""

country_list = ["Ukraine", "Spain", "Italy"]
dictionary = {country_list[0]: "Kyiv",
              country_list[1]: "Madrid",
              country_list[2]: "Rome"}
for key, value in dictionary.items(): print(key, value, sep=": ", end="\n")