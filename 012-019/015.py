#Предложите пользователю ввести любимый цвет.
#Если он введет «red», «RED» или «Red», выведите сообщение «I like red too». 
#В противном случае выведите сообщение «I don’t like [colour], I prefer red».

color = input("Введите ваш любимый цвет: ")

if(color == "red" or color == "RED" or color == "Red"):
  print("Мой любимый цвет тоже красный")

else:
  print("Мне не нравится", color, "я предпочитаю красный")