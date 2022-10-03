# Задайте список из 2N+1 элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции вводятся с клавиатуры.
from random import randint


def fill_list(n):
    for i in range(1, 2*n+2):
        list.append(randint(-n, n))
    print(list)


def multiply_list(list):
    a = int(input("Enter an index from 0 to {} > ". format(2*n+1)))
    b = int(input("Enter an index from 0 to {} > ". format(2*n+1)))
    if ((0 <= a <= 2*n+1) and (0 <= b <= 2*n+1)):
        result = list[a]*list[b]
        print(result)
    else:
        print("Incorrect a or b")


n = int(input("Enter a number > "))
if n > 0:
    list = []
    fill_list(n)
    multiply_list(list)
else:
    print("The number should be positive")
    
