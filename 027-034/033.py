# Предложите пользователю ввести два числа.
# Используйте целочисленное деление, чтобы разделить первое число на второе;
# вычислите остаток и выведите ответ в виде, удобном для пользователя
# (например, если пользователь ввел 7 и 2, выведите строку вида
# «если разделить 7 на 2, получится 3 с остатком 1»).

num1 = int(input("Введите 1 число: "))
num2 = int(input("Введите 2 число: "))

div = num1 // num2
mod = num1 % num2

print("Если разделит", num1, "на", num2, "получиться", div, "с остатоком", mod)