# Нарисуйте следующий узор:
import turtle

win = turtle.Screen()
octa = turtle.Turtle()
octa.pensize(2)
octa.speed(0)

for i in range(10):
    octa.right(36)
    for i in range(8):
        octa.forward(100)
        octa.right(45)

win.exitonclick()
