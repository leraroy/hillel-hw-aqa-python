"""
Выбрать паттерн проектирования и реализовать его на конкретном примере
(паттерн из GoF, который рассматривали или не рассматривали, но не Singleton, не Iterator, не Decorator).
"""
"""
Factory Design
"""
from abc import ABCMeta, abstractmethod


class IApartment(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def get_describe():
        "A static interface method"


class SmallApartment(IApartment):

    def __init__(self):
        self.amount_room = 1
        self.total_area = 25
        self.bathroom = 1

    def get_describe(self):
        return {
            "amount room": self.amount_room,
            "total area": self.total_area,
            "bathroom": self.bathroom
        }


class MediumApartment(IApartment):
    def __init__(self):
        self.amount_room = 2
        self.total_area = 50
        self.bathroom = 1

    def get_describe(self):
        return {
            "amount room": self.amount_room,
            "total area": self.total_area,
            "bathroom": self.bathroom
        }


class BigApartment(IApartment):
    def __init__(self):
        self.amount_room = 3
        self.total_area = 100
        self.bathroom = 2

    def get_describe(self):
        return {
            "amount room": self.amount_room,
            "total area": self.total_area,
            "bathroom": self.bathroom
        }


class ApartmentFactory:

    @staticmethod
    def get_apart(apartment):
        if apartment == "Small":
            return SmallApartment()
        if apartment == "Medium":
            return MediumApartment()
        if apartment == "Big":
            return BigApartment()
        print("Invalid apartment")
        return -1


apartment = ApartmentFactory.get_apart("Small")
print(f"{apartment.__class__.__name__} has {apartment.get_describe()}")
