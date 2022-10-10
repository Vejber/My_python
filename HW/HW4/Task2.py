# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

from sympy import isprime


def print_factors(num):
    list = []
    i = 1
    while i <= num:
        if num % i == 0 and isprime(i):
            list.append(i)
        i += 1
    print(list)


num = int(input("Enter a positive number > "))
if num > 0:
    print_factors(num)
else:
    print("Number should be above zero.")
