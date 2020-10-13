# Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

user_time = int(input("Please enter time in seconds  "))
h = user_time // 3600
m = (user_time - h * 3600) // 60
sec = user_time - (h * 3600 + m * 60)
print(f"{h} : {m} : {sec}")
