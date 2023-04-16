# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
#     60 -> 10  40  10

# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*
# 385916 -> yes
# 123456 -> no

# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no


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
   number = input('Введите трехзначное число: ')
   if len(number) != 3:
    print("Введено не трехзначное число")
   else:
    sum1 = int(number[0])+int(number[1])+int(number[2])
    print(sum1)

#Задача 4.
def task2():  
  res = int(input("Введите общее количество журавликов:"))
  if  res%6 ==0:
   petya = serj = res//6
   katya = res//6*4
   print(f'Общее количество {res}', f': Петя -> {petya},Катя ->  {katya},Сережа ->  {serj}')
  else:
     print('Введено некорректное число журавликов') 
  

#Задача 6.
def task3():
  number = input('Введите шестизначное число: ')
  if len(number) != 6:
    print("Введено не шестизначное число")
  else:  
   left = number[:3]
   rigth = number[3:]
   if left == rigth:
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

