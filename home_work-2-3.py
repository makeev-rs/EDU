# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

m = int(input("Пожалуйста введите номер месяца"))
my_dict = {1: 'winter', 2: 'winter', 3: 'spring', 4: 'spring', 5: 'spring', 6: 'summer', 7: 'summer',
           8: 'summer', 9: 'autumn', 10: "autumn", 11: 'autumn', 12: 'winter'}
my_list = list(my_dict.values())
if 12 >= m >= 1:
    print(my_dict.get(m))
for i, el in enumerate(my_list):
    if i == m - 1:
        print(f"Month from list is {my_list[i]}")
