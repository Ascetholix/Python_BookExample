# Нарисуйте пятиконечную звезду.
import turtle

win = turtle.Screen()
str = turtle.Turtle()
str.pensize(2)
str.speed(0)
str.color("red")
str.penup()
str.goto(-100, 0)
str.pendown()

for i in range(5):
    str.forward(200)
    str.right(180-36)

win.mainloop()
