"""
Написать функцию, которая принимает несколько последовательностей,
и возвращает список из кортежей составленных из элементов
последовательностей одного индекса.

Функция также должна принимать параметры с дефолтными значения:
full=False - по умолчанию "склеить" послдовательности по
кратчайшей, иначе по самой длинной

default=None - если full=True, вместо недостающих элементов
поставить значение указанное в параметре default

Встроенную функцию zip не использовать.

def custom_zip(*sequences, full=False, default=None):
    pass

seq1 = [1, 2, 3, 4, 5]
seq2 = [9, 8, 7]
assert custom_zip(seq1, seq2) == [(1, 9), (2, 8), (3, 7)]
assert custom_zip(seq1, seq2, full=True, default="Q") == [(1, 9), (2, 8), (3, 7), (4, 'Q'), (5, 'Q')]
"""


def custom_zip(*sequences, full=False, default=None):
    iters = [iter(seq) for seq in sequences]
    min_len = min(len(it) for it in sequences)
    max_len = max(len(it) for it in sequences)
    lst = []
    if full:
        for i in range(max_len):
            lst.append(tuple([next(itr, default) for itr in iters]))
        return lst
    else:
        for i in range(min_len):
            lst.append(tuple([next(itr) for itr in iters]))
        return lst


seq1 = [1, 2, 3, 4, 5]
seq2 = [9, 8, 7]

assert custom_zip(seq1, seq2) == [(1, 9), (2, 8), (3, 7)]
assert custom_zip(seq1, seq2, full=True, default="Q") == [(1, 9), (2, 8), (3, 7), (4, 'Q'), (5, 'Q')]
