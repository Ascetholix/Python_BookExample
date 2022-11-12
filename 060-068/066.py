# Нарисуйте восьмиугольник, все стороны которого окрашены в разные
# цвета (случайно выбираемые из списка шести возможных цветов)
import turtle
import random

win = turtle.Screen()
octa = turtle.Turtle()
octa.pensize(2)
octa.speed(2)


for i in range(8):
    col = random.choice(["red", "green", "yellow", "blue", "black", "orange"])
    octa.color(col)
    octa.forward(100)
    octa.right(45)

win.exitonclick()
