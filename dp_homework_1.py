# Задача 1. На вход поступает число: найти сумму цифр числа,
# в том числе если оно отрицательное или вещественное. (float)

# Задача 2. На вход поступает вещественное число, найти первую цифру дробной части.

# Задача 3. На вход поступает десятичное число, вывести его в виде двоичного

from decimal import Decimal

Menu = '''
Выберите номер задачи:
1. Нахождение суммы цифр числа.
2. Нахождение первую цифру дробной части вещественного числа.
3. Перевод десятичного числа в двоичное .
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

#Задача 1.
def task1():  
 number = (input("Введите число: "))
 digits_sum = 0
# Приводим число к строке и перебираем все символы
 for digit in str(number):
# Если символ это цифра, то добавляем ее к сумме
  if digit.isdigit():
   digits_sum += int(digit)
 print("Сумма цифр числа", number, "равна", digits_sum)



#Задача 2.
def task2():  
  number = (input("Введите число: "))
  a, b =number.split(".")
  print(f'Первая цифра дробной части {b[0]}')


#Задача 3.
def task3():
  num = int(input("Введите число: "))
  double_code = ""
  while num > 0:
   double_code = str(num % 2) + double_code
   num = num // 2
  print("Двоичное представление числа: ", double_code)

start()


               