# Нарисуйте цифры, изображенные ниже, начиная
# от нижней точки цифры 1.
import turtle

win = turtle.Screen()
num = turtle.Turtle()
num.speed(0)

num.penup()
num.goto(-200, -100)
num.pendown()

num.left(90)
num.forward(200)

num.penup()
num.right(90)
num.forward(100)
num.pendown()

num.forward(100)
num.right(90)
num.forward(100)
num.right(90)
num.forward(100)
num.left(90)
num.forward(100)
num.left(90)
num.forward(100)

num.penup()
num.forward(100)
num.pendown()

num.forward(100)
num.left(90)
num.forward(100)
num.left(90)
num.forward(50)
num.left(180)
num.forward(50)
num.left(90)
num.forward(100)
num.left(90)
num.forward(100)

num.hideturtle()  # метод скрытия черепахи

win.exitonclick()
