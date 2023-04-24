"""
Напишите функцию read_last(file_path, symbol_number), которая выводить на
печать построчно последние symbol_number символов в каждой строке
(перевод строки не учитывать).

Пустые строки - пропускать.

def read_last(file_path, symbol_number):
    pass

read_last('read_last.txt', 6)

read_last.txt ->
456789
345678
234567
Line5
"""

def read_last(file_path, symbol_number):
    with open(f'files/{file_path}') as file:
        for line in file:
            if line.strip():
                print(line[-symbol_number-1:], end='')

file_path = 'read_last.txt'
print(f"{file_path} ->")
read_last(file_path, 6)

