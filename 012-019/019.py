#Предложите пользователю ввести значение 1, 2 или 3.
#Если введено значение 1, выведите сообщение «Thank you»;
#если 2 — сообщение «Well done»;
#если 3 — сообщение «Correct».
#Если введено любое другое значение, выведите сообщение «Error message».

num = input("Ввидите число 1, 2 или 3: ")

if(num == "1"):
  print("Спасибо")
elif(num == "2"):
  print("Отлично сработано")
elif(num == "3"):
  print("Правильный")
else:
  print("Сообщение об ошибке")