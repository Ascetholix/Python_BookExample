# Предложите пользователю ввести число от 10 до 20.
# Если введенное значение меньше 10, выведите сообщение «Too low» и предложите
# повторить попытку.
# Если введенное значение больше 20, выведите сообщение «Too high» и предложите
# повторить попытку.
# Повторяйте до тех пор, пока не будет введено значение из диапазона от 10 до 20,
# после чего выведите сообщение «Thank you».

num = int(input("Введите число от 10 до 20: "))

while (num < 10 or num > 20):
    
    if (num < 10):
        print("Мало")
    else:
        print("Много")
    num = int(input("Введите число: "))
print("Спасибо")
