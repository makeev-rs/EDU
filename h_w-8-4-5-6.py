# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

# Продолжить работу над первым заданием.
# Разработать методы, отвечающие за приём оргтехники на склад и передачу
# в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.

# Продолжить работу над вторым заданием.
# Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад,
# нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники»
# максимум возможностей, изученных на уроках по ООП.


import collections


class Warehouse():
    def __init__(self, name):
        self.name = name = name
        self.items = []

    def __str__(self):
        ost = f'остатки "{self.name}":\n'
        if self.items:
            for i, item in enumerate(self.items):
                ost += f"{i}: {item}\n"
        else:
            ost += 'нет в наличии!\n'
        return ost

    def debit(self, equipment):
        self.items.append(equipment)


class Equipment():
    def __init__(self, brand, model, price):
        if not ((type(price) is int or type(price) is float) and price > 0):
            raise ValueError('price should be positive number')

        self.brandname = brand
        self.model = model
        self.price = price

    def __str__(self):
        return f'{self.itemname} {self.model} цена {str(self.price)} ₽'

    # краткое наименование
    def shortname(self):
        return f'{self.itemname} {self.model}'


class Printer(Equipment):
    itemname = 'Принтер'


class Scanner(Equipment):
    itemname = 'Сканер'


class mfu(Equipment):
    itemname = 'мфу'


e1 = Printer('HP', 'mf 452', 52000)
print(e1)

e2 = Scanner('Epson', 'scan 300', 8254)
print(e2)

e3 = mfu('hp', '440', 27000)
print(e3)

warehouse_main = Warehouse('Центральный склад')
warehouse_vlk = Warehouse('Склад Владивосток')

warehouse_main.debit(e1)
warehouse_main.debit(e2)
warehouse_main.debit(e3)

print(warehouse_main)

print(warehouse_vlk)

print(warehouse_main)

print(warehouse_main)

print(warehouse_main)

try:
    e4 = mfu('hp', '440', 32000)
    print(e4)
except ValueError as e:
    print(e)
