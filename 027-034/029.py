# Предложите пользователю ввести целое число больше 500.
# Вычислите квадратный корень из этого числа и выведите его
# с точностью до двух знаков в дробной части

import math

num = int(input("Введите число больще 500: "))

square = math.sqrt(num)

print(round(square, 2))
