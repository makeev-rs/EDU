#Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369

n = int(input("Please enter any number n: "))
x = str(n)
t1 = x + x
t2 = x + x + x
comp = n + int(t1) + int(t2)
print("You result :", comp)