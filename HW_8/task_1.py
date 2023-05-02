"""
Написать декоратор с параметром. Если применить его к
функции, он будет выводить в файл, который передали
параметром, сколько раз вызывалась функция на момент вызова.

@call_counter('data.txt')
def add(a, b):
    return a + b

print(add(4, 6))
print(add(4, 6))
data.txt content:

Function 'add' was called 1 times
Function 'add' was called 2 times
"""


def call_counter(file):
    def param(func):
        def wrapper(*args, **kwargs):
            lst = []
            with open(file, 'a') as f:
                pass

            with open(file, 'r') as f:
                for i in f:
                    if f'{func.__name__}' in i:
                        lst.append(i)
            if not lst:
                counter = 0
            else:
                counter = int(lst[-1].replace('\n', '').split()[-2])

            with open(f'{file}', 'a') as f:
                f.write(f"Function '{func.__name__}' was called {counter + 1} times\n")
            return func(*args, **kwargs)

        return wrapper

    return param


@call_counter('data.txt')
def add(a, b):
    return a + b


@call_counter('data.txt')
def sub(a, b):
    return a - b


print(add(45, 45))
print(sub(75, 65))
print(add(8, 6))
