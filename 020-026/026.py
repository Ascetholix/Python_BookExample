#В шифре «поросячья латынь» начальная согласная буква слова перемещается в конец слова,
#и к ней добавляется суффикс «ay».
#Если слово начинается с гласной, к нему просто добавляется суффикс «way».
#Например, pig превращается в igpay, banana — в ananabay, а aardvark — в aardvarkway.
#Напишите программу, которая предлагает пользователю ввести слово и преобразует
#его в «поросячью латынь».
#Проследите за тем, чтобы новое слово выводилось в нижнем регистре.
# A, E, I, O, U, Y

text = input("Введите слово: ")
text = text.lower()
first = text[0]
n = len(text)

# if(first =="a" or first == "i" or first == "y" ):
#   text = text + "way"
#   print(text)
# elif(first == "e" or first == "o" or first== "u" ):
#   text = text + "way"
#   print(text)
# else:   
#   text = text[1:n] + first + "ay"
#   print(text)

if(first !="a" and first !="i" and first !="y" and first !="e" and first !="o" and first !="u"):
  text = text[1:n] + first + "ay"
  print(text)
else:
  text = text + "way"
  print(text)
  
 