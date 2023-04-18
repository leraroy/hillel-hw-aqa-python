"""
Выборка из списка словарей
Есть список состоящий из словарей. Каждый
словарь описывает пользователся и имеет два ключа: 'name' (str) и 'age' (int).
Создать и вывести список имен пользователей чей возраст от 18 лет (включительно).

users = [
{'name': 'Luarvik L. Luarvik',
'age': 17},
{'name': 'Olaf Andvarafors',
'age': 18},
{'name': 'Brun Du Barnstokr',
'age': 19}
]
"""

users = [
{'name': 'Luarvik L. Luarvik',
'age': 17},
{'name': 'Olaf Andvarafors',
'age': 18},
{'name': 'Brun Du Barnstokr',
'age': 19}
]

lst_name = []
for i in users:
    if i.get("age") >= 18:
        lst_name.append(i.get("name"))
print(f"Cписок имен пользователей чей возраст от 18 лет:\n{lst_name}")
