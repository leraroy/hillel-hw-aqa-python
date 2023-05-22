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

    def to_dict(self):
        def filter_attribute(field_name: str):
            class_name = type(self).__name__
            start_with = '_' + class_name
            if start_with in field_name:
                return field_name.replace(start_with + '__', '')
            elif field_name.startswith('_'):
                return field_name[1:]
            else:
                return field_name

        return {filter_attribute(key): value for key, value in self.__dict__.items()}

    def __str__(self):
        class_name = type(self).__name__
        attributes = [f"{key}: {value}" for key, value in self.to_dict().items()]
        return class_name + ": {\n\t" + '\n\t'.join(attributes) + "\n}"


class A(AttributePrinterMixin):
    def __init__(self):
        self.public_filed = 3
        self._protected_field = 'q'
        self.__private_field = [1, 2, 3]


a = A()
print(a)
