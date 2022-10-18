#  Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# *Пример:*

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


# def fill_list(number):
#     n = 1
#     list = []
#     for i in range(1, number+1):
#         n = n * i
#         list.append(n)
#     print(list)


# number = int(input("Enter a number > "))
# fill_list(number)

import math


def fill_list(number):
    li = []
    j = 1
    while j <= number:
        li.append(j)
        j += 1
    print(li)
    li = list(map(lambda i: math.factorial(i), li))
    print(li)


number = int(input("Enter a number > "))
fill_list(number)
