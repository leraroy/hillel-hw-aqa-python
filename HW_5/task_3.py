"""
Есть список из не менее, чем двух float элементов.

Создать новый список, в котором между элементами
исходного списка будут добавлены их средние значения.


lst = [3.5, 2, 4, 6.2, 8] ->
[3.5, 2.75, 2, 3.0, 4, 5.1, 6.2, 7.1, 8]
"""

lst = [3.5, 2, 4, 6.2, 8]
copy_lst = lst.copy()
new_lst = []
for idx, elem in enumerate(lst):
    next_elem = copy_lst[(idx + 1) % len(copy_lst)]
    new_lst.append(elem)
    new_lst.append((elem+next_elem)/2)

new_lst.pop()
print(f"lst = {lst} ->\n{new_lst}")


