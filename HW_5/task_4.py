"""
Есть двумерный список из латинских букв,
отсортировать буквы по колонкам.

Считаем, что список прямоугольный.


[['a', 'c', 'd']
 ['f', 'b', 'a']
 ['a', 'n', 'k']
 ['e', 'l', 'i']]
->
[['a', 'b', 'a']
 ['a', 'c', 'd']
 ['e', 'l', 'i']
 ['f', 'n', 'k']]
"""

lst = [
 ['a', 'c', 'd'],
 ['f', 'b', 'a'],
 ['a', 'n', 'k'],
 ['e', 'l', 'i']]

for i in lst:
    print(i)

res = [[0 for j in range(len(lst[0]))] for i in range(len(lst))]

for j in range(len(lst[0])):
    col_values = []
    for i in range(len(lst)):
        col_values.append(lst[i][j])
    col_values.sort()
    for ii in range(len(lst)):
        res[ii][j] = col_values[ii]
print("->")

for i in res:
    print(i)