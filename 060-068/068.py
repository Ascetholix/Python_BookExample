# Нарисуйте узор, который меняется при каждом запуске программы.
# Используйте функцию random для выбора количества линий,
# длины каждой линии и каждого угла поворота.
import turtle, random

win = turtle.Screen()
ran = turtle.Turtle()
lines = random.randint(5,20)

for i in range(0,lines):
  ran.forward(random.randint(25,100))
  ran.right(random.randint(1,365))

win.exitonclick()