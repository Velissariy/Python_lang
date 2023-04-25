import random

Menu = '''
Выберите номер задачи:
1. Нахождение суммы цифр числа.
2. Нахождение первую цифру дробной части вещественного числа.
3. Перевод десятичного числа в двоичное .
'''

def start():
 while True:
    number = input('Выберите задачу: ')
    if number.isdigit() and 0 < int(number) <= 3:
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

#Задача_1. Хакер Василий получил доступ к классному журналу и хочет заменить все свои 
# минимальные оценки на максимальные. Напишите программу, которая заменяет оценки Василия, 
# но наоборот: все максимальные – на минимальные.

def task1():
    size = int(input('Введите количество оценок: '))
    max_value = int(input('Введите максимальное значение: '))
    min_value = int(input('Введите минимальное значение: '))

    my_list=[random.randint(min_value, max_value) for _ in range(size)]
    print(my_list)


    for i in range(len(my_list)):
        if my_list[i] == max_value:
            my_list[i] = min_value
    print(my_list)                      


#Задача_2. Напишите функцию, которая принимает одно число и проверяет, является ли оно простым      

def task2():
  number = int(input('Введите число: '))
  count=0
  for item in range(1, number+1):
     if number%item ==0:
        count+=1
  if count==2:
     print('число является простым')
  else:
     print('число не является простым')

#  k = 0
#  for i in range(2, number // 2+1):
#     if number % i == 0:
#         k = k+1

#  if k <= 0:
#     print("Число простое")
#  else:
#     print("Число не является простым")        



# Задача_3. Дано натуральное число N и последовательность из N элементов.
# Требуется вывести эту последовательность в обратном порядке.              
def task3():
  n=10

  rev_list=[]
  my_str=' '              


  def Reverse(n):
     if n==1:
        return 1
     else:
        return my_str += my_str + Reverse(n-1)  
  
  my_str +=Reverse(10)        