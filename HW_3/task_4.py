"""
Пользователь вводит минимальную и максимальную ширину "бриллиантового" паттерна.

Вывести "бриллиант" с заданными размерами составленный из символов '*'

Если введенная минимальная ширина больше максимальной ширины,
вывести предупреждение и завершить программу.

Если разность максимальной и минимальной ширины не кратно 2,
вывести предупреждение (через print) и завершить программу.

> Enter minimal width: 3
> Enter maximal width: 5
 ***
*   *
 ***
> Enter minimal width: 1
> Enter maximal width: 3
 *
* *
 *
> Enter minimal width: 2
> Enter maximal width: 6
  **
 *  *
*    *
 *  *
  **
> Enter minimal width: 3
> Enter maximal width: 9
   ***
  *   *
 *     *
*       *
 *     *
  *   *
   ***
"""

min_width = int(input('Enter minimal width: '))
max_width = int(input('Enter maximal width: '))

if min_width > max_width:
    print("Error: the minimal width is greater than the maximal width")
    quit()

if (max_width - min_width) % 2 != 0:
    print("Error: the difference between the minimal and minimal width is not a multiple of 2")
    quit()

for i in range(min_width, max_width+1, 2):
    if i == min_width:
        print(("*" * i).center(max_width))
    else:
        print(("*" + " "*(i-2) + "*").center(max_width))

for j in range(max_width-1, min_width, -2):
    if j == min_width+1:
        print(("*" * min_width).center(max_width))
    else:
        print(("*" + " "*(j-3) + "*").center(max_width))













