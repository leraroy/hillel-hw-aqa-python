"""
Написать функцию, которая принимает параметром функцию и произвольное число последовательностей.

Если передается одна последовательность, то надо вернуть список,
в котором будет результат применения функции к каждому
 элементу последовательности.
Если передается несколько последовательностей, то
переданная функция должна иметь такое же количество
аргументов. В этом случае надо вернуть список, который будет
состоять из результатов выполнения функции, в которую передали
первые элементы всех последовательностей, затем вторые, и т. д.

Если переданные последовательности разной длины, то
результат сформировать по кратчайшему.

Встроенную функцию map не использовать.

def custom_map(function, *sequences):
    pass

assert custom_map(sum, [[1, 2, 3], [4, 5]]) == [6, 9]
assert custom_map(lambda x, y: x + y, [1, 2, 3, 4], (3, 4, 4, 4, 4, 4, 44)) == [4, 6, 7, 8]
"""


def custom_map(function, *sequences):
    result = []
    if len(sequences) > 0:
        min_len = min(len(subseq) for subseq in sequences)
        for i in range(min_len):
            result.append(function(*[subseq[i] for subseq in sequences]))
    return result


assert custom_map(sum, [[1, 2, 3], [4, 5]]) == [6, 9]
assert custom_map(lambda x, y: x + y, [1, 2, 3, 4], (3, 4, 4, 4, 4, 4, 44)) == [4, 6, 7, 8]