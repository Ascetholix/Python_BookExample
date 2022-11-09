# Выведите названия пяти цветов, случайным образом выберите один
# и предложите сделать то же пользователю.
# Если пользователь выберет тот же цвет, который выбрала программа,
# выведите сообщение «Well done»;
# в противном случае выведите ответ, в котором скрывается намек на правильный цвет.
# Предложите пользователю повторить попытку; если пользователь и на этот раз не угадает,
# снова выведите ту же подсказку и предложите выбрать цвет
# (и так далее, пока пользователь не выдаст правильный ответ).
import random

color = random.choice(["красный", "белый", "черный", "серый", "желтый"])
print("красный, белый, черный, серый, желтый")
answer = input("Выберите цвет:")

if (answer == color):
    print("ВЫ ПОБЕДИЛИ")
else:
    while (color != answer):
        if (color == "красный"):
            print("он 1 в списке")
        elif (color == "белый"):
            print("он 2 в списке")
        elif (color == "черный"):
            print("он 3 в списке")
        elif (color == "серый"):
            print("он 4 в списке")
        else:
            print("он 5 в списке")
        answer = input("Выберите цвет:")
print("Правильный ответ - ", answer)
