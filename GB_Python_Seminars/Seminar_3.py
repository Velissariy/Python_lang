import random

def start():
 while True:
    number = input('Выберите задачу: ')
    if number.isdigit() and 0 < int(number) <= 4:
       break
    else:
       print('Введите корректный номер задачи: ')
 match int(number):
              case 1:
               task11()
              case 2:
               task1()
              case 3:
               task2()
              case 4:
               task3()
              case 5:
               task4()
#Задача 1.
# Дан список чисел. Определите, сколько в нем встречается различных чисел.

def task1():
 list_1 = [7, 9, 11, 13, 15, 17, 7, 11]
 print(*list_1)
 print(len(set(list_1)))

def task11():
 list_num = (input('Введите список чисел: '))
 uniq_list = []
 for item in list_num:
    if not item in uniq_list:
        uniq_list.append(item)
 print(list_num)
 print(uniq_list)

#Задача 2.
# Дана последовательность из N целых чисел и число K.
# Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо, 
# K – положительное число.

def task2():
 list_num = (input('Введите список чисел: '))        
 k = int(input('Введите k: '))
 # omega = list_num[::-1]
 list_num=list_num[-k:] + list_num[:-k]
 print(list_num)

#Задача 3.
# Дан список, состоящий из целых чисел. 
# Напишите программу, которая подсчитает количество элементов списка, 
# больших предыдущего (элемента с предыдущим номером)

def task3():
 num_list=[1,2,3,4,5,6,4,3,4,]
 count=0
 k=len(num_list)-1
 for i in range(k):
     if num_list[i]<num_list[i+1]:
      count+=1

 print(count)     

#Задача 4.
# my_list = [{"V": "S001"}, {"V": "S002"},
#            {"VI": "S001"}, {"VI": "S005"},
#            {"VII": "S005"}, {" V ": "S009"},
#            {" VIII ": "S007"}]
# Напишите программу для печати всех уникальных значений в словаре.

def task4():
 my_list = [{"V": "S001"}, {"V": "S002"},
           {"VI": "S001"}, {"VI": "S005"},
           {"VII": "S005"}, {" V ": "S009"},
           {" VIII ": "S007"}]
 uniq = set()

 for item in my_list:
    for value in item.values():   #items(), keys()
       uniq.add(value)
 print(uniq)
  