# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит натуральное
# число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#
# *Пример:*
#
# 5
#     1 2 3 4 5
#     3
#     -> 1
#
from random import randint
# lenth_list = int(input('Введите длину списка : '))
#
# number = []
# for i in range(1):
#     number.append(int(input('Ведите число которое хотите проверить : ')))
#
# my_list = []
# for j in range(lenth_list):
#     my_list.append(randint(1, lenth_list))
#
# count = 0
# for k in range(len(my_list)):
#     if my_list[k] == number[i]:
#         count += 1
#
# print(f'Исходный список : {my_list}')
# print(f'Цифра {number} встречается {count} раз')

# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой
# строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#
# *Пример:*
#
# 5
#     1 2 3 4 5
#     6
#     -> 5
#
# my_list = []
# for i in range(10):
#     my_list.append(randint(1,15))
# print(my_list)
# num = int(input('Введите число : '))
# min_dist = float('inf')
# result =my_list[0]
# for i in my_list:
#     if abs(num -i) < min_dist :
#         min_dist = abs(num -i)
#         result  = i
# print(result)
#
# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L,N, S, T, R –1 очко; D, G –
# 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков. А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка; Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков. Напишите программу,
# которая вычисляет стоимость введенного пользователем слова. Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.
#
# *Пример:*
#
# ноутбук
#     12
# dictionary = {1: 'AEIOULNSTRАВЕИНОРСТ',
#               2: 'DGДКЛМПУ',
#               3: 'BCMPБГЁЬЯ',
#               4: 'FHVWYЙЫ',
#               5: 'KЖЗХЦЧ',
#               8: 'JXШЭЮ',
#               10: 'QZФЩЪ'}
#
# word = input('введите слово :').upper()
# summ = 0
# for i in word :
#     for k, v in dictionary.items() :
#         if i in v :
#             summ += k
# print(summ)

#
# import random
# kust = int(input("введите количество кустов: "))
# berryes = list(random.randint(0, 10) for i in range(kust))
# result = []
# i = 0
# sum = 0
#
# print(berryes)
#
# while (i < kust):
#     if (i == kust - 1):
#         sum = berryes[i] + berryes[i - 1] + berryes[0]
#     else:
#         sum = berryes[i] + berryes[i - 1] + berryes[i + 1]
#         result.append(sum)
#         result.sort()
#     i += 1
#
# print(f"максимальное число ягод за одну итерацию {result[-1]}")
#
#
n1 = int(input('Введите количество элементов первого набора чисел: '))
n2 = int(input('Введите количество элементов второго набора чисел: '))
arr1 = []
arr2 = []
for i in range(n1):
    arr1.append(int(input('Введите элемент первого массива: ')))
for j in range(n2):
    arr2.append(int(input('Введите элемент второго массива: ')))
arr3 = []
for i in arr1:
    if i in arr2 and i not in arr3:
            arr3.append(i)
arr3.sort()
print(arr3)
