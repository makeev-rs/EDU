# Создать текстовый файл (не программно),
# сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.
my_file = open('hw-5-1.txt', 'r', encoding='utf-8')
content = my_file.read()
print(f'Содержимое файла: \n {content}')
my_file = open('hw-5-1.txt', 'r', encoding='utf-8')
content = my_file.readlines()
print(f'Кол-во строк в файле - {len(content)}')
my_file = open('hw-5-1.txt', 'r', encoding='utf-8')
content = my_file.readlines()
for i in range(len(content)):
    print(f'кол-во символов {i + 1} - ой строки {len(content[i])}')
my_file = open('hw-5-1.txt', 'r', encoding='utf-8')
content = my_file.read()
content = content.split()
print(f'Общее кол-во  слов - {len(content)}')
my_file.close()
