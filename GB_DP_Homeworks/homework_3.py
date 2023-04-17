# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в списке A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в списке. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# Пример:
#     1 2 3 4 5
#     3 -> 1

# Задача 18: Требуется найти в списке A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в списке. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# Пример:
#     1 2 3 4 5
#     6 -> 5

# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
# В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко; D, G – 2 очка; B, C, M, 
# P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков.
# А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь,
# Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

# Пример:
# ноутбук
#     12

import random

Menu= '''
Выберите номер задачи:
1. Программа для нахождения определенного числа в заданном списке.
2. Программа для нахождения самого близкого определенного числа в заданном списке.
3. Программа, которая считает стоимость слова по определенным спискам.
'''
print(Menu)

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

#Задача 1.
def task1():
  number = int(input('Введите число N(длина списка): '))
#   int_list=[1,number+1]
  desired_number = int(input('Введите искомое число: '))
  count=0
  for i in range(1, number+1):
      if desired_number==i:
         count += 1
  print(*range(1,number+1))
  print(f'{desired_number} -> {count}')    

#Задача 2.
def task2():
    
 user_list_length = int(input('Введите количество элементов в списке: '))
 user_list = [random.randint(0, user_list_length) for i in range(user_list_length)]
 print(user_list)
 user_element_search = int(input('Для какого элемента будем искать ближайшее значение -> '))
 nearest_element_minimum, nearest_element_maximum = user_element_search - 1, user_element_search + 1
 flag = True
 while flag:
    for i in user_list:
        if i == nearest_element_minimum:
            print(f"Ближайший минимальный элемент {i}")
            flag = False
            break
    for i in user_list:
        if i == nearest_element_maximum:
            print(f"Ближайший максимальный элемент {i}")
            flag = False
            break
    nearest_element_minimum -= 1
    nearest_element_maximum += 1 

#Задача 3.
def task3():
    
    english_values = {'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8, 'K': 5,
                  'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4,
                  'W': 4, 'X': 8, 'Y': 4, 'Z': 10}

    russian_values = {'А': 1, 'Б': 3, 'В': 1, 'Г': 3, 'Д': 2, 'Е': 1, 'Ё': 3, 'Ж': 5, 'З': 5, 'И': 1, 'Й': 4,
                  'К': 2, 'Л': 2, 'М': 2, 'Н': 1, 'О': 1, 'П': 2, 'Р': 1, 'С': 1, 'Т': 1, 'У': 2, 'Ф': 10,
                  'Х': 5, 'Ц': 5, 'Ч': 5, 'Ш': 8, 'Щ': 10, 'Ъ': 10, 'Ы': 4, 'Ь': 3, 'Э': 8, 'Ю': 8, 'Я': 3}

    word = input('Введите слово: ')

    total_score = 0

    for i in word:
     if i.upper() in english_values:
        total_score += english_values[i.upper()]
     elif i.upper() in russian_values:
        total_score += russian_values[i.upper()]
    print('Стоимость слова "{}" равна {} очкам.'.format(word, total_score))               


start()
