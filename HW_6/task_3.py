"""
Есть текстовый файл. Вывести самую длинную строку.
Функции max, readlines не использовать. Файл может быть большим.
"""
res = []
has_line = True
max_line = ''
max_ = 0
with open("files/file_task_3.txt") as my_file:
    while has_line:
        line = my_file.readline()
        if not line:
            break
        lines = line.replace('\n', '')
        res.append(lines)
        if (len(lines)) > max_:
            max_ = len(lines)
            max_line = lines
print(f"Самая длинная строка\n{max_line}")
