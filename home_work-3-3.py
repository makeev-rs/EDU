# Реализовать функцию my_func(),
# которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
def my_func(a, b, c):
    my_list = [a, b, c]
    total = []
    max_1 = max(my_list)
    total.append(max_1)
    my_list.remove(max_1)
    max_2 = max(my_list)
    total.append(max_2)
    print(sum(total))


my_func(1, 8, 20)
