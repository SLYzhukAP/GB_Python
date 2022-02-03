# Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.
num1 = int(input('Введите число: '))
str = str(num1)
str2 = int(str + str)
str3 = int(str + str + str)
summa = int(int(str) + int(str2) + int(str3))
print(summa)
