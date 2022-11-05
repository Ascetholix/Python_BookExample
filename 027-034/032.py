# Предложите пользователю ввести радиус и высоту цилиндра.
# Вычислите его объем (площадь круга * высота) и выведите его
# с точностью до трех знаков
import math

radius = float(input("Введите радиус цилиндра: "))
height = float(input("Введите высоту цилинндра: "))

pi = math.pi
areaСircle = (radius**2) * pi

volume = areaСircle * height

print("Объем цилиндра = ", round(volume, 3))