# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой
def my_func(name, surname, year, city, email, phone):
    print(name, surname, year, city, email, phone)


my_func(name='Ruslan', surname='Makeev', year=1980, city='Vlk', email='email', phone='666')
