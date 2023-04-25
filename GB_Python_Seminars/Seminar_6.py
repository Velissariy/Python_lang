from decimal import Decimal
import random
from random import randint
import math

Menu = '''
Выберите номер задачи:
1. Нахождение уникальных элементов 1 списка, которых нет во 2 списке.
2. Программа, которая определит два соседних и, при этом,два соседних элемента меньше данного.
3. Программа, которая посчитает количество пар чисел в списке.
4. Эталонное питоновское решение 3 задачи.
5. Программа, которая выводит все пары дружественных чисел в заданном списке.
'''

def start():
 while True:
    print(Menu)
    number = input('Выберите задачу: ')
    if number.isdigit() and 0 < int(number) <= 5:
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
               task3_1()
              case 5:
               task4() 

def new_list(minn,maxx,length):           
      a =[randint(minn,maxx) for i in range(length)]
      return a

def promt(msg):
      a = int(input(msg))  
      return a

def uniq_list(list1, list2):
      uniq_list=list()
      for item  in list1:
         if item not in list2:
            uniq_list.append(item)
      return uniq_list
# Задача_1. Даны два массива чисел. Требуется вывести те элементы первого массива 
# (в том порядке, в каком они идут в первом массиве), которых нет во втором массиве
def task1():
 
   first_list = new_list(1,10,10)
   second_list=new_list(1,5,10)
   print(first_list,second_list, uniq_list(first_list,second_list),sep="\n")      

  #  list1=[random.randint(0,10) for _ in range(5)]
  #  list2=[random.randint(0,10) for _ in range(5)]
  #  print(list1, list2)

  #  for i in list1:
  #     if i not in list2:
  #        print(i, end=" ")

  #  print(i for i in list1 i, end =' ' if i not in list2)   

# Задача_2.
#  Дан массив, состоящий из целых чисел. Напишите программу,
#  которая в данном массиве определит количество элементов,
#  у которых два соседних и, при этом, оба соседних элемента меньше данного.
def task2():
   my_list = [randint(10,20) for i in range(15)]
   count=0
   print(my_list)

   for i in range(1, len(my_list)):
      if my_list[i-1] < my_list[i] > my_list[i+1]:
         count+=1
   print(f'Количество элементов в списке: {count}') 
   #complecation
   a = [1 for i in range(1,len(my_list)-1) if my_list[i]<my_list[i]>my_list[i+1]]      
   print(f'Количество элементов в списке: {len(a)}')

# Задача_3.
# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. 
# Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать. 
# Вводится список чисел. Все числа списка находятся на разных строках.

def uniq_dictionary(list1):
      uniq_dict={}
      for number in list1:
         uniq_dict[number] = uniq_dict.get(number, 0) +1
      print(uniq_dict)
      return uniq_dict

def uniq_pairs(dict_n: dict, count=0):
      for values in dict_n.values():
         if values//2==0:
            count+=values//2
      return count

def task3():
  my_list = new_list  
  a = new_list(1,10,15)
  print(a)
  new_dict = uniq_dictionary(a)
  b = uniq_pairs(new_dict)
  print(b)
  
  #  lst = [randint(1,10) for i in range(10)]
  #  print(lst)
  #  dct = dict()
  #  for i in range(len(lst)):
  #   dct[lst[i]]=lst.count(lst[i])//2 
  #  print(dct)
# Эталонное решение. 
def task3_1():
  my_list = [random.randint(0,10) for _ in range(30)]
  print(my_list)
  repeats = sum([my_list.count(item)//2 for item in set(my_list)])
  print(repeats)

# Задача_4
# Два различных натуральных числа n и m называются дружественными, 
# если сумма делителей числа n (включая 1, но исключая само n) равна числу m и наоборот. 
# Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k.
# Программа получает на вход одно натуральное число k, не превосходящее 105. 
# Программа должна вывести все пары дружественных чисел, каждое из которых не превосходит k.
# Пары необходимо выводить по одной в строке, разделяя пробелами. 
# Каждая пара должна быть выведена только один раз (перестановка чисел новую пару не дает).

def summarize(num,sum=0):
   for item in range(1,num//2+1):
      if num%item ==0:
         sum +=item
   return sum

def task4():
   k=300
   my_list = [i for i in range(k)]
   print(my_list)
   for item in my_list:
      if item == summarize(summarize(item)) and item !=summarize(item):
        print(item, summarize(item))
  
start()
   
       