# Нарисуйте круг
import turtle

scr = turtle.Screen()  # оперделить окно с названием scr

circ = turtle.Turtle()  # переменая хранения туртле
circ.speed(20)
circ.pensize(1)

# circ.circle(100)       # метод circle(радиус круга)

for i in range(40):
    circ.circle(100)       # метод circle(радиус круга)
    circ.right(10)

scr.mainloop()          # Функция mianloop что бы окно не заерывалось
