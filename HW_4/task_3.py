"""
В программе есть строка s.

Вывести заголовком строку, котрая состоит из слов, в которых буква 'a'
встречается два раза.

s = "aab qq c badcc a qqqqqaqqqqaa tpara"
Aab Tpara
"""

s = "aab qq c badcc a qqqqqaqqqqaa tpara"
list_words = s.split(' ')

result = []
for i in list_words:
    if i.count('a') == 2:
        result.append(i.title())
print(" ".join(result))


