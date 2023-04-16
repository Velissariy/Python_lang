from decimal import Decimal
import random
from random import randint

Menu = '''
Выберите номер задачи:
1. Факториал.
2. Порядок числа Фиббоначи.
3. Нахождение количества теплых дней.
3.1. Нахождение количества теплых дней.(Альтернатива)
5. Находим рандомные оптималльные арбузы.
'''

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
               task31()
              case 5:
               task4()   

#Задача 1.
#Факториал
def task1(): 

 my_limit = int(input('Введите предел факториала: '))
 fact = 1
 count = 1
 while count <=my_limit:
    fact*=count
    count+=1
 print(fact) 

#Задача 2.
# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, 
# то есть выведите такое число n, что φ(n)=A.
# Если А не является числом Фибоначчи, выведите число -1.

def task2(): 
 n1=0
 n2=1
 k=2
 a = int(input('Введите число: '))
 while n2 <a:
    n1, n2 =n2, n2+n1
    k+=1
 if n2 !=a:
    print("-1")
 else:
    print(k)

#Задача 3.
# Уставшие от необычно теплой зимы, жители решили узнать, действительно ли это самая длинная оттепель за всю историю
# наблюдений за погодой. Они обратились к синоптикам, а те, в свою очередь, занялись исследованиями статистики за прошлые годы.
# Их интересует, сколько дней длилась самая длинная оттепель.
# Оттепелью они называют период, в который среднесуточная температура ежедневно превышала 0 градусов Цельсия.
# Напишите программу, помогающую синоптикам в работе.

def task3(): 
   
 length = 30
 count = 0
 max_count = 0
 today = 0
 for i in range(length):
    today += random.randint(-3,3)
    print(today, end=" ")
    if today >0:
        count +=1
        if count > max_count:
           max_count = count
    else:
        count=0
 print(f"\nМаксимальное число тёплых дней: {max_count}")

def task31(): #Албтернативное решение:
 len_ght = 30
 I = 1
 otp = 0
 max_otp = 0

 while I <= 30:
    temp = random.randint(-5,10)
    print(temp,end = " ")
    if temp > 0:
        otp = otp+1

        if otp > max_otp:
            max_otp = otp
    else:
        otp = 0
    I = I + 1
 print()
 print("Максимальная длинна оттепели",max_otp)

#Задача 4.
# Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи. 
# Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче. 
# Но вот незадача: арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел, записанных на новой строчке каждое.
# Здесь каждое число – это масса соответствующего арбуза. Все числа натуральные и не превышают 30000.

def task4():

 MAX_WEIGTH = 30000
 MIN_WEIGTH = 1000

 watermelon = int(input("Введите количество арбузов: "))
 weigth = 0
 max_weigth = MIN_WEIGTH
 min_weigth = MAX_WEIGTH
 for i in range(watermelon):
    weigth = random.randint(MIN_WEIGTH,MAX_WEIGTH)
    print(weigth, end=" ")
    if weigth > max_weigth:
            max_weigth = weigth
    if weigth < min_weigth:
          min_weigth = weigth
 print(f"\nАрбуз для себя получился на {max_weigth}грамм, а для тёщи {min_weigth}грамм. ")
               