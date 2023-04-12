# Задача 1. На вход поступает число: найти сумму цифр числа, 
# в том числе если оно отрицательное или вещественное. (float)

# Задача 2. На вход поступает вещественное число, найти первую цифру дробной части.

# Задача 3. На вход поступает десятичное число, вывести его в виде двоичного

import math

Menu= '''
Выберите номер задачи:
1. Нахождение суммы цифр трехзначного числа.
2. Сколько журавликов сделал каждый ребенок.
3. Программа, которая проверяет счастливость билета.
4. Определить, можно ли от шоколадки размером n × m долек отломить k долек.
'''
print(Menu)

def start():
 while True:
    number = input('Выберите задачу: ')
    if number.isdigit() and 0 < int(number) <= 4:
       break
    else:
       print('Введите корректный номер задачи: ')
 match int(number):
              case 1:
               task1()
              case 2:
               task2()
              case 3:
               task3()
              case 4:
               task4()

#Задача 2.
def task1():
   a = input('Введите трехзначное число: ')
   if len(a) != 3:
    print("Введено не трехзначное число")
   else:
    sum1 = int(a[0])+int(a[1])+int(a[2])
    print(sum1)

#Задача 4.
def task2():  
  res = int(input("Введите общее количество журавликов:"))
  kef = math.ceil(res/6)
  p = 1*kef
  k = 4*kef
  s = 1*kef
  print(f'{res}', f'->: {p}  {k}  {s}')

#Задача 6.
def task3():
  a = input('Введите шестизначное число: ')
  if len(a) != 6:
    print("Введено не шестизначное число")
  else:
    sum1 = int(a[0])+int(a[1])+int(a[2])
    sum2 = int(a[3])+int(a[4])+int(a[5])
    if sum1 == sum2:
        print('yes')
    else:
        print('no')

#Задача 8.
def task4():
  n = int(input("Введите количество долек по горизонтали: "))
  m = int(input("Введите количество долек по вертикали: "))
  k = int(input("Введите количество долек, которые надо отломать: "))

  if (n * m-1) >= k and (k % n == 0 or k % m == 0):
    print("можно отломать", k, "долек одним разломом")
  else:
    print("нельзя отломать", k, "долек одним разломом")

start()