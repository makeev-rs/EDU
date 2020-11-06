import sys


class Myexception:
    def __init__(self, *args):
        self.my_list = []

    def my_input_list(self):

        while True:
            try:
                n = int(input('Вводите числа  и нажимайте Enter:  '))
                self.my_list.append(n)
                print(f'Текущий список - {self.my_list} \n ')
            except:
                print(f" - строка   или булево")
                y_or_n = input(f'Попробовать еще раз? Y/N ')

                if y_or_n == 'Y' or y_or_n == 'y':
                    print(try_except.my_input_list())
                elif y_or_n == 'N' or y_or_n == 'n':
                    exit(0)


try_except = Myexception(1)
print(try_except.my_input_list())
