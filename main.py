# задание1
# n = input("Введите трехзначное число: ")
# n = int(n)
 # d1 = n % 10
# n = n // 10
# d2 = n % 10
# d3 = n % 10
# n = n // 10
 
# print(f'сумма цифр числа : {n+d2+d3}')

# s = int(input(" введите число :"))
# sergey = s / 6
# petr = sergey
# ekaterina = (sergey + petr) * 2
# print(int(sergey), int(ekaterina),int(petr))

# t = input('Введите номер билета: ')
# l = int(t[0]) + int(t[1]) + int(t[2])
# r = int(t[3]) + int(t[4]) + int(t[5])
# if l == r:
#     print('Yes')
# else:
# #     print('NO')

# s = input('Введите 6-значный номер билета: ')
# if len(s) != 6 :
#     print(f'Число {s} не 6-ти значное')
# else:
#     res1 = 0
#     res2 = 0
#     for i in range(len(s)//2):
#         res1 += int(s[i])
#         res2 += int(s[len(s)//2 + i])
#     if res1 == res2:
#         print(f'{s} счастливый номер')
#     else:
#         print(f'{s} не счастливый номер')

#  Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no
#
# n = int(input(" введите длину :"))

# m = int(input("введите ширину :"))

# k = int(input(" введите количество долек"))

# if (n * m ) - k > 0  and ( k % n == 0 or k % m == 0 ):
#     print( "yeeeesss : ")
# else:
#     print("noooy :")


# data = [1, 2, 3, 5, 8, 15, 23, 38,]
# res = list()

# for i in data:
#     if i % 2 == 0:
#         res.append((i, i**2))

# print(res)


# import random
# kust = int(input("введите количество кустов: "))
# berryes = list(random.randint(0, 10) for i in range(kust))
# result = []
# i = 0
# sum = 0

# print(berryes)

# while (i < kust):
#     if (i == kust - 1):
#         sum = berryes[i] + berryes[i - 1] + berryes[0]
#     else:
#         sum = berryes[i] + berryes[i - 1] + berryes[i + 1]
#         result.append(sum)
#         result.sort()
#     i += 1

# print(f"максимальное число ягод за одну итерацию {result[-1]}")

list=[-5,9,0,3,-1,-2,1,4,-2,10,2,0,-9,8,10,-9,0,-5,-5,7]
min_number = int(input())
max_number = int(input())
for i in range(len(list)):
    if min_number <= list[i] <= max_number:
        print(i)