# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# *Пример:*

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
def fill_list(n):
    for i in range(1, n+1):
        list.append(int(input("Enter a number > ")))
    print(list)


def odd_sum(list):
    sum = 0
    for i in range(1, len(list)):
        if i % 2 != 0:
            sum += list[i]
    print("The total of odd elements in list is {}.".format(sum))


number = int(input("Enter the length of the list > "))
list = []
if number > 0:
    fill_list(number)
    odd_sum(list)
else:
    print("The length should be positive.")
