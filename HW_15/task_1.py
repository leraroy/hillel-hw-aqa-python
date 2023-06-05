"""
Написать декоратор, который будет кешировать результат
выполнения функции.
При первом вызове, функция должна выполниться и результат
сохраниться в памяти.
При следующих вызовах он должен извлекаться из памяти,
если функция вызывается с теми же аргументами.
"""


class CasheDecorator:

    def __init__(self, func):
        self.func = func
        self.dict = {}

    def __call__(self, *args, **kwargs):
        args_ = str(args)
        kwargs_ = str(sorted(kwargs.items()))
        key_dict = args_ + kwargs_
        if key_dict in self.dict.keys():
            return self.dict[key_dict]
        else:
            result = self.func(*args, **kwargs)
            self.dict[key_dict] = result
            return result


@CasheDecorator
def add(a, b):
    return a + b


@CasheDecorator
def func_with_kwargs(*args, **kwargs):
    return args, kwargs


print(add(4, 7))
print(add(3, 7))
print(add(10, 7))
print(add(3, 7))
print(func_with_kwargs('first', a=3, b=4))
print(func_with_kwargs('first', a=23, b=34))
print(func_with_kwargs('first', b=4, a=3))
