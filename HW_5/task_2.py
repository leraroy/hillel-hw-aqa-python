"""
Найти сумму и произведение элементов списка больше числа MIN и меньше числа MAX (включительно).

Если таких элементов нет, вывести ноль и для суммы, и для произведения.


lst = [2, 4, 6, 2, 1, 1, 9, 4, 6], MIN = 3, MAX = 6
sum_ = 20, product = 576
"""

lst = [2, 4, 6, 2, 1, 1, 9, 4, 6]
MIN = 3
MAX = 6
sum_ = 0
product = 1
count = 0
for i in lst:
    if MAX >= i >= MIN:
        sum_ += i
        product *= i
        count += 1
print(f"list = {lst}, MIN = {MIN}, MAX = {MAX}")
if count > 0:
    print(f"sum_ = {sum_}\nproduct = {product}")
else:
    print(f"sum_ = {0}\nproduct = {0}")

