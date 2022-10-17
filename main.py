# easy code for Random Generate Number
# python learning 
# aleksandrgill 

from random import randint # подключаем библиотеку рандинт из рандома

print("Генератор рандомных чисел.")

n = int(input("Укажите сколько рандомных чисел нужно вывести: "))
count = int(input("Укажите диапозон. От 1 до ... ? "))
for i in range(n):
  a = randint(1, count+1)
  print("Результат:", a)

