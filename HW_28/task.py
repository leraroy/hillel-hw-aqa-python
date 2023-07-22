"""
Написать класс для работы с таблицей БД.
Таблица должна создаваться при инстанцировании класса
(при повторном инстанцировании не должен выбрасываться
эксепшен о том что таблица уже создана).

В классе должны быть методы:

- для получения всех записей в виде списка объектов пользовательских классов;
- добавление одной/нескольких записей по переданным объектам;
- обновление записи/записей по условию (условие на свой выбор)
- получение записей по условию (условие на свой выбор)
- удаление записей по условию (условие на свой выбор)
- по желанию добавить еще методы/классы, которые сделают работу с таблицей проще
"""
import sqlite3
from random import *

from faker import Faker

fake = Faker()


class RandomData:

    def __init__(self):
        self.name = fake.name()
        self.phone = fake.phone_number()
        self.email = fake.ascii_free_email()
        self.state = fake.state()
        self.price = randint(1, 99999)
        self.discount = 0

    def get_random_attributes(self):
        return self.name, self.phone, self.email, self.state, self.price, self.discount


class Customer:

    def __init__(self, name='', phone='', email='', state='', price=0, discount=0):
        self.name = name
        self.phone = phone
        self.email = email
        self.state = state
        self.price = price
        self.discount = discount

    def __repr__(self):
        return f"Customer(name={self.name}, phone={self.phone}, email={self.email}, address={self.state}, price={self.price}, discount={self.discount})\n"

    def get_customer_attributes(self):
        return self.name, self.phone, self.email, self.state, self.price, self.discount


class AbstractRepository:

    def __init__(self, db_path):
        self.connection = sqlite3.connect(db_path, isolation_level=None)
        self.cursor = self.connection.cursor()

    def __del__(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()


class CustomersTable(AbstractRepository):

    def __init__(self, db_path):
        super().__init__(db_path)
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS Customers(id INTEGER PRIMARY KEY, name TEXT NOT NULL UNIQUE, phone TEXT, email TEXT, state TEXT, price REAL, discount INTEGER);")

    def add_customer(self, customer: Customer):
        self.cursor.execute(
            "INSERT INTO Customers(name, phone, email, state, price, discount) VALUES ((?), (?), (?), (?), (?), (?));",
            customer.get_customer_attributes())

    def add_customers(self, customers):
        self.cursor.executemany(
            "INSERT INTO Customers(name, phone, email, state, price, discount) VALUES ((?), (?), (?), (?), (?), (?));",
            [customer.get_customer_attributes() for customer in customers])

    def update_customer_by_id(self, id, name_field, value):
        self.cursor.execute(
            f'UPDATE Customers SET {name_field} = "{value}" WHERE id = {id}')

    def update_customers_discount_by_price(self, min_price_for_discount, add_discount):
        self.cursor.execute(
            f"UPDATE Customers SET discount = {Customer().discount + add_discount} WHERE price >= {min_price_for_discount}")

    def get_all_records(self):
        data = self.cursor.execute("SELECT * FROM Customers")
        return self.rows_to_objects(data)

    def get_customers_by_state(self, state):
        data = self.cursor.execute(f'SELECT * FROM Customers WHERE state="{state}";')
        return self.rows_to_objects(data)

    def get_customers_by_name(self, name):
        data = self.cursor.execute(f'SELECT * FROM Customers WHERE name="{name}";')
        return self.rows_to_objects(data)

    def get_customer_by_id(self, id):
        data = self.cursor.execute('SELECT * FROM Customers WHERE id=(?);', (id,))
        return self.rows_to_objects(data)

    def delete_by_id(self, id):
        self.cursor.execute(f"DELETE FROM Customers WHERE id={id};")

    def delete_by_name(self, name):
        self.cursor.execute(f"DELETE FROM Customers WHERE name LIKE '%{name}%';")

    def delete_table(self):
        self.cursor.execute("DROP TABLE Customers;")

    def row_to_object(self, row):
        return Customer(*row[1:])

    def rows_to_objects(self, rows):
        return [self.row_to_object(row) for row in rows]


customers = CustomersTable("dbs/orders.db")
customer1 = Customer(*RandomData().get_random_attributes())

customers_list = [
    Customer(*RandomData().get_random_attributes()),
    Customer(*RandomData().get_random_attributes()),
    Customer(*RandomData().get_random_attributes())
]
customers.add_customer(customer1)
customers.add_customers(customers_list)
print(customers.get_all_records())
print(customers.get_customer_by_id(3))
customers.update_customer_by_id(3, "phone", "+785-358-4695")
print(customers.get_customer_by_id(3))
print(customers.get_all_records())
customers.update_customers_discount_by_price(95000.0, 20)
print(customers.get_all_records())
print(customers.get_customers_by_state("Tennessee"))
print(customers.get_customers_by_name("Ashley Clark"))
print(customers.get_all_records())
customers.delete_by_id(8)
print(customers.get_all_records())
customers.delete_by_name("Evan Lee")
