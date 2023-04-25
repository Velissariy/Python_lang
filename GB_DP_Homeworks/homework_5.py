# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 

# Задача 28: Напишите рекурсивную функцию summ(a, b), 
# возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# *Пример:*
# 2 2
#     4 

def raisedegree(a, b):
    if b == 0:
        return 1
    elif b % 2 == 0:
        return raisedegree(a * a, b // 2)
    else:
        return a * raisedegree(a, b - 1)

def summ(a, b):
    if b == 0:
        return a
    elif a == 0:
        return b
    else:
        return summ(a ^ b, (a & b) << 1)
    

Menu = '''
Выберите номер задачи:
1. Программа,которая возводит число А в целую степень B с помощью рекурсии.
2. Рекурсивная функция sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
'''

def start():
 print(Menu)
 while True:
    number = input('Выберите задачу: ')
    if number.isdigit() and 0 < int(number) <= 2:
       break
    else:
       print('Введите корректный номер задачи: ')
 match int(number):
              case 1:
               task1()
              case 2:
               task2()

def task1():

 a = int(input("Введите число A: "))
 b = int(input("Введите число B: "))

 result = raisedegree(a, b)
 print(f"{a} в степени {b} равно {result}")

def task2(): 
 
 a = int(input("Введите первое число: "))
 b = int(input("Введите второе число: "))
 result = summ(a, b)
 print(f"Сумма чисел {a} и {b} равна {result}")
start() 

             