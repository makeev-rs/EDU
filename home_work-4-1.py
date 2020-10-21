# Реализовать скрипт, в котором должна быть предусмотрена
# функция расчета заработной платы сотрудника. В расчете
# необходимо использовать формулу:
# (выработка в часах*ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо
# запускать скрипт с параметрами.

from sys import argv

name, hour, price, benefit = argv
try:
    hour = int(hour)
    price = int(price)
    benefit = int(benefit)
    total = hour * price + benefit
    print(f'заработная плата включая премию {total}')
except ValueError:
    print('Error')
