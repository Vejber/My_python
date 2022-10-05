# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# *Пример:*

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from random import uniform


def fill_list(n):
    for i in range(1, n+1):
        list.append(round(uniform(1.10, 10.10), 2))
    print(list)


def max_min_diff(list):
    result = []
    for i in range(len(list)):
        result.append(round(list[i] - int(list[i]), 2))
    print(result)
    max = result[0]
    min = result[0]
    for i in range(len(result)):
        if result[i] > max:
            max = result[i]
        if result[i] < min:
            min = result[i]
    print(min, max)
    print(round((max-min), 2))


number = int(input("Enter the length of the list > "))
list = []
if number > 0:
    fill_list(number)
    max_min_diff(list)
else:
    print("The length should be positive.")
