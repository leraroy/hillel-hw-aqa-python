"""
Создать два класса, предметную область выбрать по своему желанию.

Классы должны содержать:
- минимум два поля экземпляров и одно поле класса
- минимум два метода экземпляра

Хотя бы в одном классе:
- минимум один метод класса
- минимум один статический метод
К методам добавить строки документации.

Методы должные быть НЕ get/set поле, а что-то оригинальнее:)
(но если надо их, тоже можно добавить)
Написать код который создает несколько экземпляров
и взаимодействует с объектами
"""

from datetime import datetime


class Person:

    def __init__(self, first_name, last_name, birthday_date):
        self.first_name = first_name
        self.last_name = last_name
        self.birthday_date = birthday_date

    @classmethod
    def from_string_to_date(cls, str_date):
        return datetime.strptime(str_date, '%d.%m.%Y').date()

    @staticmethod
    def get_age(birthday_date):
        birth_date = Person.from_string_to_date(birthday_date)
        today = datetime.today()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        return age

    def is_adult(self):
        if Person.get_age(self.birthday_date) >= 18:
            return True
        return False


person_1 = Person("Sam", "Smith", "04.11.1999")
person_2 = Person("John", "Brown", "15.12.2012")
person_3 = Person("Nina", "Stanley", "25.05.2020")

print(f"Age: {person_1.get_age(person_1.birthday_date)}")
print(f"{person_1.first_name} {person_1.last_name} is adult - {person_1.is_adult()}")


class Employee(Person):
    id = 0
    employees = []

    def __init__(self, first_name, last_name, birthday_date, salary, department):
        super().__init__(first_name, last_name, birthday_date)
        Employee.id += 1
        self.id = Employee.id
        self.salary = salary
        self.department = department
        Employee.employees.append({
            "id": self.id, "name": self.first_name + " " + self.last_name, "birthday_date": self.birthday_date,
            "salary": self.salary, "department": self.department
        })

    def change_department(self, department):
        self.department = department
        for emp in Employee.employees:
            if emp["name"] == self.first_name + " " + self.last_name:
                emp["department"] = self.department

    def get_age_employee(self):
        return self.get_age(self.birthday_date)

    def print_data_about_employee(self):
        print(f"ID: {self.id}")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Salary: {self.salary}")
        print(f"Department: {self.department}")

    def calculate_salary(self, hours_worked):
        if hours_worked > 50:
            self.salary = self.salary + ((hours_worked - 50) * (self.salary / 50))


employee_1 = Employee("Sam", "Smith", "25.12.1999", 2000, "QA")
employee_2 = Employee("Kate", "Brown", "12.12.1992", 5000, "SEO")
employee_3 = Employee("Paul", "Johnson", "12.12.1975", 3000, "HR")

print(employee_1.employees)
employee_1.change_department("Sales")
employee_1.print_data_about_employee()
print(f"\nAge employee {(employee_2.get_age_employee())}\n")
employee_2.calculate_salary(70)
employee_2.print_data_about_employee()
