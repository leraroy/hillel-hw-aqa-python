"""
Пользователь вводит строку. Вывести True, если строка является палиндромом,
иначе False.

Палиндром - строка, которя читается одинаково слева и справа.

Если в строке есть ведущие или конечные пробелы, они не учитываются.

Проверка должна быть регистронезависимой.

Решить минимум двумя способами.

"    aBC cba " # True
"a BCQcb a    " # True
" ab bca"  # False
"""


str1 = input("Enter string: ")
str_without_space = str1.strip().lower()
# version 1

str2 = str_without_space[::-1]
print(True) if str_without_space == str2 else print(False)

# version 2
str3 = ''.join(reversed(str_without_space))
print(str_without_space == str3)

# version 3
res_str = ""
for i in str_without_space:
    res_str = i + res_str

if res_str == str_without_space:
    print(True)
else:
    print(False)








