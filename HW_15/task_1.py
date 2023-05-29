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
        kwargs_ = str(kwargs)
        key_dict = args_ + kwargs_
        if key_dict in self.dict.keys():
            return self.dict[key_dict]
        else:
            self.dict[key_dict] = self.func(*args, **kwargs)
            return self.func(*args, **kwargs)


@CasheDecorator
def add(a, b):
    return a + b


print(add(4, 7))
print(add(3, 7))
print(add(10, 7))
print(add(3, 7))
