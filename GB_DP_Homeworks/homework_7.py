# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, 
# Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв)
# в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, 
# если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами.
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”,
# если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке
# Пример:
# Ввод: пара-ра-рам рам-пам-папам па-ра-па-да
# Вывод: Парам пам-пам

# Задача 36: Напишите функцию `print_operation_table(operation, num_rows=6, num_columns=6)`,
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.
# Аргументы `num_rows` и `num_columns` указывают число строк и столбцов таблицы, которые должны быть распечатаны.
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, 
# как, например, у операции умножения.
# Пример:
# Ввод: `print_operation_table(lambda x, y: x * y) `
# Вывод: 1 2 3 4 5 6

# 2 4 6 8 10 12
# 3 6 9 12 15 18
# 4 8 12 16 20 24
# 5 10 15 20 25 30
# 6 12 18 24 30 36

Menu = '''Выберите номер задачи:
1. Программа, которая посчитает ритм в предложении Винни-Пуха.
2. Функция, которая которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.'''

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


def count_vowels_consonants(poem):
 vowels = "aeiouyAEIOUY"
 consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
 count_v = 0
 count_c = 0
 for letter in poem:
  if letter in vowels:
   count_v += 1
  elif letter in consonants:
   count_c += 1
 return count_v, count_c

    
def print_operation_table(operation, num_rows=6, num_columns=6):
     for i in range(1, num_rows + 1):
        row = []
        for j in range(1, num_columns + 1):
            row.append(str(operation(i, j)))
        print("\t".join(row))   

def multiply(a, b):
     return a * b

def task1():
    poem = input("Введите стихотворение: ")
    count_v, count_c = count_vowels_consonants(poem)
    if count_v > count_c:
     print("Пам парам")
    elif count_v < count_c:
     print("Пам парам")
    else:
     print("Парам пам-пам")
 
def task2():
    a = int(input("Введите количество строк: "))
    b = int(input("Введите количество столбцов: "))
    print_operation_table(multiply, a, b)

start()





