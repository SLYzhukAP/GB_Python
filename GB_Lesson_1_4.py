# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции

num_in = int(input("Введите число: "))
m = -1
while num_in > 10:
    d = num_in % 10
    num_in //= 10
    if d > m:
        m = d
print ('Самая большая цифра в вашем числе: ', m)