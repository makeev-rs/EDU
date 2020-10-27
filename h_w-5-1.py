# Создать программно файл в текстовом формате,
# записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.
my_file = open('hw-5-1.txt', 'w', encoding='utf-8')
line = " "
while line:
    line = input(' Please input any text: ')
    my_file.write(f"{line}\n")
    if not line:
        break
my_file.close()
with open('hw-5-1.txt') as f_obj:
    for line in f_obj:
        print(line)
