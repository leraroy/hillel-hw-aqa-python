"""
Написать функцию, на вход которой передают список чисел,
а возвращает второе по величине число.

Если передали пустой список, функция должна вернуть None.

Из встроенных функций можно использовать только range и len.

Написать реализацию, которая выполняет только один проход списка.


def second_largest_number(lst):
    pass

second_largest_number([4, 2, 1, 5, 2, 5, 7])  # 5
second_largest_number([])  # None
"""

def second_largest_number_without_method_sort(lst_numbers):
    lst_without_duplicate = []
    if len(lst_numbers) > 0:
        for i in range(len(lst_numbers)):
            for j in range(i + 1, len(lst_numbers)):
                if lst_numbers[i] > lst_numbers[j]:
                    lst_numbers[i], lst_numbers[j] = lst_numbers[j], lst_numbers[i]
            if lst_numbers[i] not in lst_without_duplicate:
                lst_without_duplicate.append(lst_numbers[i])
        return lst_without_duplicate[len(lst_without_duplicate)-2]
    return None

def second_largest_number_with_method_sort(lst_numbers):
    lst_without_duplicate = []
    if len(lst_numbers) > 0:
        lst_numbers.sort()
        for i in lst_numbers:
            if i not in lst_without_duplicate:
                lst_without_duplicate.append(i)
        return lst_without_duplicate[len(lst_without_duplicate)-2]
    return None

print(second_largest_number_with_method_sort([4, 2, 1, 5, 2, 5, 7]))
print(second_largest_number_without_method_sort([4, 2, 1, 5, 2, 5, 7]))




