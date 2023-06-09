# Задача 1. ПАЛИНДРОМЫ
# а) на вход подается слово - проверить, является ли оно палиндромом
# Например на слово  ‘довод’ выводит  ‘да’, а на слово  ‘повод’ - нет.
# Больше примеров слов-палиндромов  
# довод, доход, заказ, кабак, комок, мадам, олололо, потоп, радар, ротатор, топот, шалаш
# level deified noon Racecar radar repaper
# б) на вход подается фраза - проверить, является ли она палиндромом
# Не учитывается регистр, знаки препинания и пробелы.
# Примеры фраз-палиндромов
# А роза упала на лапу Азора
# Я иду с мечем судия
# Хил, худ, а дух лих. ——> точки и запятые?
# Тарту дорог, как город утрат
# А путана тупа
# И темен город. Мороз, узором дорог не мети.
# Леша на полке клопа нашел.
# Аргентина манит негра
# Straw? No, too stupid a fad. I put soot on warts
# Was it a cat I saw?
# Do geese see God?
# Madam, I'm Adam 
# Pull up if I pull up
# No lemon, no melon
# SATOR AREPO TENET OPERA ROTAS


# Задача 2. ТАБЛИЦА УМНОЖЕНИЯ
# Напишите программу, которая будет выводить в консоль таблицу умножения от 1 до 10 
# (как в вконце старых тетрадок, квадратная такая


# Задача 3. ИСТИННОСТЬ ПРЕДИКАТ
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# Данное выражение истинно при любых значениях предикат (предикат - переменная, которая может иметь
# только два значения True или False)
# Напишите программу, которая докажет это.
# https://ru.wikipedia.org/wiki/Список_логических_символов - вот вам ссылочка, если непонятно, что за символы)


# Задача 4. СПОРТСМЕНЫ
# На вход подается возраст и вес спортсмена. Вывести группу по возрасту и весовую категорию, в которой он будет принимать участие согласно следующим правилам.
# Соревнования юношей младшей возрастной группы (14—15 лет) проводятся без деления 
# участников на весовые категории. 
# Соревнования для юношей старшего возраста (16—17 лет) проводятся в весовых категориях:
# легчайшая - до 52 кг
# легкая - до 57
# средняя - до 70
# тяжёлая - до 80
# вторая тяжелая свыше 80
# Соревнования для юниоров (18—19 лет) и взрослых (20 лет и старше) 
# легчайшая - до 54 кг
# легкая - до 60
# средняя - до 75
# тяжелая свыше 81
# Лица младше 14 или весом ниже 44 кг до соревнований не допускаются


# Задача 5. FIZZ BUZZ
# Напишите программу, которая выводит на экран числа от 1 до n. 
# При этом вместо чисел, кратных трем, программа должна выводить слово «Fizz», 
# а вместо чисел, кратных пяти — слово «Buzz». Если число кратно и 3, и 5, то программа должна выводить слово «FizzBuzz»

# Задача 6. ПРОСТЕЙШИЙ КАЛЬКУЛЯТОР
# Написать программу, которая выполняет над двумя вещественными числами одну из четырех арифметических операций
# (сложение, вычитание, умножение или деление):
# вводим первое число, 
# потом операцию
# и второе число
# выводится результат

# Программа должна завершаться только по желанию пользователя:
# можно ввести enter и программа закончится, или еще операцию и еще число. Ну и помним, что на ноль делить нельзя.

Menu = '''
Выберите номер задачи:
1. Программа, которая проверяет слово - является ли оно палиндромом.
2. Программа, которая выводит в консоль таблицу умножения от 1 до 10. 
3. Программа, которая докажет истинность предиката.
4. Программа, которая определит кандидата в возрастную группу соревнований.
5. Программа, которая выводит на экран числа от 1 до n.
6. Программа, которая простейший калькулятор.
'''
print(Menu)

def start():
 while True:
    number = input('Выберите задачу: ')
    if number.isdigit() and 0 < int(number) <= 6:
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
              case 6:
               task6()

#Задача 1.
def task1():  
 omega = (input("Введите слово или фразу: "))
 omega = omega.replace(" ","").lower()
 if omega == omega[::-1]:
    print('yes')
 else:
    print('no')


# Задача 2.
def task2():  
  for i in range(1, 10):
     for j in range(1, 10):
      print(f'{i}x{j}={i*j}', end='   ')
     print()

# Задача 3.
def task3(): 
  X = True
  Y = True
  Z = True
  left_value = not(X or Y or Z)
  right_value = not(X) and not(Y) and not(Z)
  if left_value == right_value:
    print("¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z  -> Выражение верно")
  else:
    print("¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z  ->  Выражение неверно")

#Задача 4.
def task4():
  age = float(input("Введите возраст: "))
  weigth = float(input("Введите вес: "))
  if  14 <= age <16:
    print(f'Соревнования юношей младшей возрастной группы')
  if 16<=age <18:
     print(f'Соревнования для юношей старшего возраста')
     if weigth <=52:
      print(f'Легчайшая категория')
     if  52 < weigth <=57:
      print(f'Легкая категория')
     if 57 < weigth <=70:
      print(f'Средняя категория')
     if 70 < weigth <=80:
      print(f'Тяжелая категория')
     if 80 < weigth:
      print(f'Вторая тяжелая категория')
  if 18<=age <20 or age >= 20:
     print(f'Соревнования для юниоров и взрослых') 
     if weigth <=54:
      print(f'Легчайшая категория')
     if  54 < weigth <=60:
      print(f'Легкая категория')
     if 60 < weigth <=75:
      print(f'Средняя категория')
     if 81 < weigth:
      print(f'Тяжелая категория')
  if  14 > age:
    print(f'До соревнований не допущен по возрасту')
  if weigth < 44:   
    print(f'До соревнований не допущен по весу')

#Задача 5.
def task5():
 n = int(input("Введите число n: "))
 for i in range(1,n+1):
    if i%5==0 and i%3 ==0:
       print('FizzBuzz')
    elif i%5 ==0:
        print('Buzz') 
    elif i%3 ==0:
      print('Fizz')
    else:
      print(i)
 
#Задача 6.
def task6():
 while True:
  a = float(input('Введите первое число: '))
  menushka ='''
 1.Сложение
 2.Вычитание
 3.Умножение
 4.Деление
 '''
  print(menushka)
  x = input('Выберите действие: ')
  match x:
              case 1:
               break
              case 2:
               break
              case 3:
               break
              case 4:
               break
                 
  b = float(input('Введите второе число: '))

  if x == '1':
   res= a + b
  elif x == '2':
   res= a - b
  elif x == '3':
   res= a * b
  elif x == '4':
   res= a / b
  print(res)
  value = input("Хотите продолжить? (нажмите Enter, чтобы закончить или введите 'y', чтобы продолжить): ")
  if value == "":
   break
  if value == "y":
    while True:
     print(menushka)
     x = input("Выберите действие: ")
     match x:
              case 1:
               break
              case 2:
               break
              case 3:
               break
              case 4:
               break
              case 5:
               break
     с = float(input('Введите следующее число: '))
     if x == '1':
      res= res + с
     elif x == '2':
      res= res - с
     elif x == '3':
      res= res * с
     elif x == '4':
      res= res / с
     print(res)
     value = input("Хотите продолжить? (нажмите Enter, чтобы закончить или введите 'y', чтобы продолжить): ")
     if value == "":
      break
     continue
  if value == "":
   break
  # continue
 
start()
