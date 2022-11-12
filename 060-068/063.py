# Нарисуйте в один ряд
# три квадрата, разделенных промежутками.
# Заполните их тремя разными цветами.
import turtle

scr = turtle.Screen()
qu = turtle.Turtle()
col = ["red", "yellow", "black"]  # массив цветов
qu.penup()      # поднятие ручки. не рисуем
qu.goto(-200, 0)  # переход на кординату х=-200 и у=0
qu.pensize(2)
qu.speed(0)

for i in range(3):
    qu.color(col[i])     # цвет линии

    for i in range(4):
        qu.pendown()        # отпускание ручки. рисуем
        qu.forward(100)
        qu.right(90)
    qu.penup()
    qu.forward(110)

scr.mainloop()
