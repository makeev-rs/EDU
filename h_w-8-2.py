# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно
# обработать эту ситуацию и не завершиться с ошибкой.

class DivideByZeroException(Exception):
    def __str__(self):
        return "На ноль делить нельзя"


def try_divide(num_1, num_2):
    if num_2 == 0:
        raise DivideByZeroException()
    else:
        return num_1 / num_2


while True:
    num_1 = int(input('делимое: '))
    num_2 = int(input('делитель: '))

    try:
        print('{} / {} = {}'.format(num_1, num_2, try_divide(num_1, num_2)))
    except DivideByZeroException as e:
        print(e)
