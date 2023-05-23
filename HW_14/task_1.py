"""
Написать класс-миксин, наследуя который, объект будет
выводится в консоль в виде имени класса и словаря полей
со значениями:

ClassName: {
    key: value
}

class AttributePrinterMixin:
    pass
Протектед и приватные поля должны выводить только свое имя
(без знака подчеркивания для протектед и префикса
"_<имя класса>__" для приватных)
Каждя строка с полем начинается с символа табуляции.
Если класс наслудует другие классы, их поля тоже должны
выводится по тем же правилам.
Свойства обрабатывать не надо.

Пример:

class A(AttributePrinterMixin):
    def __init__(self):
        self.public_filed = 3
        self._protected_field = 'q'
        self.__private_field = [1, 2, 3]

a = A()
print(a)


A: {
   public_filed: 3
   protected_field: q
   private_field: [1, 2, 3]
}
"""


class AttributePrinterMixin:
    def __str__(self):
        result = {}
        resulted_str = ""
        for key, value in self.__dict__.items():
            if key.startswith('_'):
                if '__' in key:
                    key = key[key.find('__') + len('__'):]
                    result[key] = value
                else:
                    result[key[1:]] = value
            else:
                result[key] = value

        for key, value in result.items():
            resulted_str += f"\n\t{key}: {value}"
        return self.__class__.__name__ + ": {" + resulted_str + "\n}"


class C(object):
    def __init__(self):
        super(C, self).__init__()
        self.__qwerty = "qwerty_in_b"


class B(object):
    def __init__(self):
        super(B, self).__init__()
        self.__privat_in_b = "privat_in_b"


class A(B, C, AttributePrinterMixin):
    def __init__(self):
        super(A, self).__init__()
        self.public_filed = 3
        self._protected_field = 'q'
        self.__private_field = [1, 2, 3]


a = A()
print(a)
