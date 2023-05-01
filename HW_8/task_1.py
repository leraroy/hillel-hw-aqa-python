"""
Написать декоратор с параметром. Если применить его к функции, он будет
выводить в файл, который передали параметром, сколько раз вызывалась
функция на момент вызова.

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
        func.counter = 0

        def wrapper(*args, **kwargs):
            func.counter += 1
            wrapper.counter.append(func.counter)
            with open(f'files/{file}', 'w') as f:
                for i in wrapper.counter:
                    f.write(f"Function '{func.__name__}' was called {i} times\n")
            return func(*args)

        wrapper.counter = []
        return wrapper

    return param


@call_counter('data.txt')
def add(a, b):
    return a + b


print(add(2, 5))
print(add(4, 6))
print(add(4, 9))
