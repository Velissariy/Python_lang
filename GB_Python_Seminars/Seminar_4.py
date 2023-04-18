
import random

Menu= '''
Выберите номер задачи:
1. Программа для нахождения определенного или самого близкого числа в заданном списке.
2. Программа, которая считает стоимость слова по определенным спискам_v1.
3. Программа, которая считает стоимость слова по определенным спискам_v2.
4. Программа, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался..
5. .
'''
print(Menu)

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

#Задача 1.
# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в списке A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в списке. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# Задача 18: Требуется найти в списке A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в списке. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

def task1():
  size = int(input('Введите размер вашего списка: ')) 
  min_limit = int(input('Введите минимальное значение: '))
  max_limit = int(input('Введите максимальное значение: '))
  
  my_list = [random.randint(min_limit, max_limit) for _ in range(size)]
  print(my_list)
  number = int(input('Введите искомое число: '))

  count = my_list.count(number)
  
  closest = my_list[0]
  if count < 1:
     for item in my_list:
        if abs(number - item) < abs(number - closest):
           closest = item
  print(f'Число {number} встречается {count} раз' if count >0 else f'Ближайшее к {number} число: {closest}')

#Задача 2.
# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
# А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

def task2():
    scrabble = { 'AEIOULNSTRАВЕИНОРСТ' : 1,
                 'DGДКЛМПУ' : 2,
                 'BCMPБГЁЬЯ': 3,
                 'FHVWYЙЫ':  4,
                 'KЖЗХЦЧ':  5 ,
                 'JXШЭЮ' : 8 ,
                 'QZФЩЪ':  10}
    
    word = input('Введите слово: ') 
    # ноутбук
    total = 0
    for letter in word.upper():
       for letters in scrabble: # проходит по ключам даже без указания key()
          if letter in letters:
              total += scrabble.get(letters)
              break
    
    print(f'Cлово "{word.upper()}" весит {total} баллов')        
    


#Задача 3.
def task3():
    
    scrabble = [( 1, 'AEIOULNSTRАВЕИНОРСТ'),
                 (2,'DGДКЛМПУ'),
                 (3,'BCMPБГЁЬЯ'),
                 (4,'FHVWYЙЫ'),
                 (5,'KЖЗХЦЧ'),
                 (8,'JXШЭЮ'),
                 (10,'QZФЩЪ')]
    
    my_dict={}
    [my_dict.update(my_dict.fromkeys(values, key)) for key, values in scrabble]
    
    word = input('Введите слово: ') 
    total = 0
    for letter in word.upper():
         total +=my_dict.get(letter)
    # word = input('Введите слово: ').upper()
    # total = sum([my_dict.get(letter) for letter in word])     
    print(f'Cлово "{word.upper()}" весит {total} баллов')

   
#Задача 4.
# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался.
# Количество повторов добавляется к символам с помощью постфикса формата _n.
def task4():

  #  Считает элементы в списке
  #  a = str(input('Type in your string: '))
  #  result = dict((i, a.count(i)) for i in a)
  #  print (result)

  #  Почти получилось
  #  text=str(input('Type in your string: '))
  #  list_dict ={} 
  #  for letter in text:
  #     list_dict[letter] = list_dict.get(letter,0)+1
  #     print(f'{letter} if {list_dict.get==0}: else _{list_dict.get(letter)}')
  #     if list_dict.get==0:
  #        print(f'{letter}')
  #     else:
  #        print(f'{letter}_{(letter)}')  

    # C count решение
    # my_list = list(input('Input list: '))
    # print(my_list[0], end=' ') 
    # for i in range(1, len(my_list)):
    #    print(f'{my_list[i]}', end=' ')
    #    count = my_list[:i-1].count(my_list[i])
    #    if count>0:
    #       print(f'_{count}', end=' ')
         
  # Более-менее решение:
  text=list(input('Input string: ')) 
  count_dict={}
  for letter in text:
     count_dict[letter] = count_dict.get(letter,0)+1
     if count_dict.get(letter)==1:
       print(f'{letter} ', end=' ')
     else:
        print(f'{letter}_{count_dict.get(letter)-1}', end=' ')
    # Используем тернарный оператор
    #  print(f'{letter}'if count_dict.get(letter)==1 else f'{letter}_{count_dict.get(letter)-1}', end=' ') 
  # print(count_dict)


start()
