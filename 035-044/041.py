# Предложите пользователю ввести имя и число.
# Если число меньше 10, программа должна вывести имя заданное количество раз;
# в противном случае она выводит сообщение «Too high» три раза.

name = input("Введите имя: ")
num = int(input("Введите число: "))

if (num < 10):
    for i in range(num):
        print(name)
else:
    for i in range(3):
        print("Too high")
