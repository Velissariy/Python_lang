# from decimal import Decimal
import math

Menu = '''
Выберите номер задачи:
1. Нахождение расстояния.
2. Нахождение нужного вагона.
3. Нахождение нужного года(високосный или нет).
4. Перевод числа десятичного в двоичное.
5. Находим количество парт для класса.
'''

def start():
 while True:
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
               task4()
              case 5:
               task5()   

#Задача 1.
# За день машина проезжает n километров. Сколько дней нужно,
# чтобы проехать маршрут длиной m километров?
# При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.

def task1(): 
  
 n = int(input("Введите n: "))
 m = int(input("Введите m: "))
 # print(f"Ответ: {int(m // n + m % n + 0.5)}")
 print(n/m)
 print(math.ceil(n/m))

#Задача 2.
# Вагоны в электричке пронумерованы натуральными числами, начиная с 1 (при этом иногда вагоны нумеруются от «головы» поезда,
# а иногда – с «хвоста»; это зависит от того, в какую сторону едет электричка).
# В каждом вагоне написан его номер. Витя сел в i-й вагон от головы поезда и обнаружил,
# что его вагон имеет номер j. Он хочет определить, сколько всего вагонов в электричке.
# Напишите программу, которая будет это делать или сообщать, что без дополнительной информации это сделать невозможно.

def task2(): 
   
 i = 6
 j = 3
 if i == j:
    print("невозможно посчитать")
 else:
    print(i + j -1)


#Задача 3.
# Дано натуральное число. Требуется определить, является ли год с данным номером високосным.
# Если год является високосным, то выведите YES, иначе выведите NO.
# Напомним, что в соответствии с григорианским календарем,
# год является високосным, если его номер кратен 4, но не кратен 100, а также если он кратен 400.


def task3():
  n = int(input('Введите натуральное число: '))
  if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
    print('Год високосный.')
  else:
    print('Год не високосный.')
#  elif year % 100 == 0:
#  if year % 400 == 0:
#         print('Год високосный.')
#  else:
#         print('Год не високосный.')
#   else:
#      print('Год високосный.')


#Задача 4.
def task4():
  num = int(input("Введите число: "))
  double_code = ""
  while num > 0:
   double_code = str(num / 2) + double_code
   num = num // 2
  print("Двоичное представление числа: ", double_code)

#Задача 5.
# В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для них новыми партами.
# За каждой партой может сидеть два учащихся. Известно количество учащихся в каждом из трех классов.
# Выведите наименьшее число парт, которое нужно приобрести для них.

def task5():
# n_1 = int(input("Введите кол-во участников: "))
 n_1 = 9
 n_2 = 7
 n_3 = 4
 res1 = ((n_1+1)//2)
 res2 = ((n_2+1)//2)
 res3 = ((n_3+1)//2)
 res = res1+res2+res3
 print(f"Ответ: {res1}+{res2}+{res3} = {res}")
start()











