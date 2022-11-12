# Нарисуйте квадрат.
import turtle

scr = turtle.Screen()

for i in range(4):
    turtle.forward(100)
    turtle.left(90)

scr.exitonclick()  # Метод exitonclick при клике окно закроеться
