"""
В программе есть строка multi_string. Строка состоит из предложений.
Предложение - это набор символов, ограниченных точками или началом строки и точкой.

Записать в список количество слов в каждом предложении.
Слово - набор символов между двумя пробелами или началом строки и пробелом.

Регулярные выражения не использовать.


multi_string = "Hello all. Here's pretty cold and hot. Choose yourself."
words_number -> [2, 5, 2]
"""

multi_string = "Hello all. Here's pretty cold and hot. Choose yourself."

result = multi_string.split('.')
result.pop()
count_words = []
for i in result:
    str_without_space = i.strip().split(' ')
    count_words.append((len(str_without_space)))

print(f"{multi_string}\nwords_number -> {count_words}")
