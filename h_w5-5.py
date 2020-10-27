# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
def summary():
    try:
        with open('h_w-5-6.txt', 'w+', encoding='utf-8') as file_obj:
            line = input('Введите цифры через пробел \n')
            file_obj.writelines(line)
            n = line.split()

            print(sum(map(int, n)))
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Неправильно набран номер. Ошибка ввода-вывода')


summary()
