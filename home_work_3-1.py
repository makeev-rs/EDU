# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль

def my_division(n, m):
    try:
        z = n / m
        return z
    except ZeroDivisionError:
        return "y is'n be a zero"


print(my_division(int(input("Enter x = ")), int(input("Enter y = "))))
