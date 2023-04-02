"""
Создать список из трех имен котов/собак

Вывести через запятую и пробел:

Murzik, Barsik, Pantera
"""

pet_list = ["Murzik", "Barsik", "Pantera"]

# version 1
print(*pet_list, sep=", ")
# version 2
print(", ".join(pet_list))
# version 3
print(f"{pet_list[0]}, {pet_list[1]}, {pet_list[2]}")

