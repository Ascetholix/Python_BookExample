
import turtle
turtle.speed(10)  # Скорость запольнения

# turtle.shape("turtle")   # внешный вид
# for i in range(5):       # пятиугольник и его цикл
#   turtle.forward(100)
#   turtle.right(72)

# turtle.exitonclick()

turtle.shape("turtle")

for i in range(10):
    turtle.right(36)

    for i in range(5):
        turtle.forward(100)
        turtle.right(72)

turtle.exitonclick()  # при клинке закрываеться окно
