# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
from random import randint


def fill_list(n):
    for i in range(1, n+1):
        list.append(randint(1, 10))
    print(list)


def pair_multiply(list):
    new_list = []
    i = 0
    j = len(list) - 1
    if len(list) % 2 == 0:
        while (len(list) // 2) <= j:
            new_list.append(list[i]*list[j])
            j = j - 1
            i = i + 1
    else:
        while (((len(list) // 2)) <= j):
            new_list.append(list[i]*list[j])
            j = j - 1
            i = i + 1

    print(new_list)


number = int(input("Enter the length of the list > "))
list = []
if number > 0:
    fill_list(number)
    pair_multiply(list)
else:
    print("The length should be positive.")
