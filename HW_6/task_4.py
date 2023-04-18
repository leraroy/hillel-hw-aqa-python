"""
Есть текстовый файл с данными пользователей.
Каждая строка определяет одного пользователя.
В строке через точку с запятой указаны имя, возраст и список
телефонов.
Если телефонов несколько, они разделены запятой.

Прочитать файл и создать список из словарей с ключами 'name', 'age', 'phones'.
По каждому ключу записать соответствующее поле из файла.
Поле имя обязательное. Если возраст или телефоны не указаны, точка с запятой все равно должны быть указаны в строке.
Имя записать в виде строки.
Возраст записать в виде целого числа. Если возраст не указан или не возможно распарсить, записать None.
Телефоны записать списком строк. Если телефоны не указаны, записать пустой список.
Если в имени или одном из телефонов есть ведущие или конечные пробелы, их надо удалить.

Полученный список:

- записать в users_out.json файл
- записать в users_out.txt файл, по правилам исходного файла (возраст None или пустой список для телефонов должны преобразовываться в пустую строку)

В исходном файле могут быть пустые строки.
Исходный файл может быть большим.
Примеры файлов прикреплены.

Пример списка:
[{'age': 34, 'name': 'user1', 'phones': ['+3804454545']},
{'age': 23, 'name': 'user2', 'phones': []},
{'age': None, 'name': 'user3', 'phones': []},
{'age': None, 'name': 'user4', 'phones': ['+5635665335']},
{'age': 25, 'name': 'user5', 'phones': ['+6563663', '+3333635635']},
{'age': None, 'name': 'user6', 'phones': []}]
"""

import json
lines = []
has_line = True
with open("files/users.txt") as my_file:
    while has_line:
        line = my_file.readline()
        if not line:
            break
        line = line.replace('\n', '').strip()
        if (len(line)) > 0:
            lines.append(line)
users_lst = []
users = []
for i in lines:
    user_dict = {}
    data = i.split(';')
    users.append(data)
    if len(data[0]) > 0:
        user_dict["name"] = data[0].strip()
    else:
        user_dict["name"] = None
    if len(data[1]) > 0 and data[1].isdigit():
        user_dict["age"] = int(data[1].strip())
    else:
        user_dict["age"] = None
    if len(data[2]) > 0:
        user_dict["phones"] = data[2].strip().replace(' ', '').split(',')
    else:
        user_dict["phones"] = []
    users_lst.append(user_dict)

with open("files/users_out.json", "w" ) as f:
        json.dump(users_lst, f)

with open("files/users_out.txt", "w") as f:
    for user in users:
        user = [x.replace(' ', '') for x in user]
        if not user[1].isdigit():
            user[1] = ''
        f.writelines(';'.join(user)+ '\n')


