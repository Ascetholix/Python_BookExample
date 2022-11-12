# Нарисуйте треугольник
import turtle

scr = turtle.Screen()

tri = turtle.Turtle()  # переменая
tri.pensize(2)        # размер линии pensize(размер линии)

for i in range(3):
    tri.forward(100)
    tri.left(180-60)  # 180 - 60 = 120 градусов

scr.exitonclick()
# scr.mainloop()
