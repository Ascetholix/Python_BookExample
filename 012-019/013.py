#Предложите пользователю ввести число, меньшее 20. 
#Если введенное число больше или равно 20, выведите сообщение «Too high»; 
#в противном случае выведите сообщение «Thank you».

num = int(input("Введите число, меньше 20: "))

if(num >= 20):
  print("Слышком много")
else:
  print("Спасибо")