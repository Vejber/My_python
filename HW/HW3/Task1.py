# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.

# *Пример:*

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
# def fill_list(n):
#     for i in range(1, n+1):
#         list.append(int(input("Enter a number > ")))
#     print(list)


# def odd_sum(list):
#     sum = 0
#     for i in range(1, len(list)):
#         if i % 2 != 0:
#             sum += list[i]
#     print("The total of odd elements in list is {}.".format(sum))


# number = int(input("Enter the length of the list > "))
# list = []
# if number > 0:
#     fill_list(number)
#     odd_sum(list)
# else:
#     print("The length should be positive.")


def fill_list(n):
    print("Enter {} elements > ".format(n))
    data = list(map(int, input().split()))
    print(data)
    return data


def odd_sum(data):
    def sum_odd(op, sum):
        return sum

    sum_odds = []

    # i = 0
    # for index in range(len(data)):
    #     sum_odds = list(filter(lambda index: index % 2, data))

    for i in range(0, len(data)-1):
        if i % 2 != 0:
            sum_odds.append(data[i])

    print(sum_odds)
    print("The total of odd elements in list is {}.".format(len(sum_odds)))

    sum = 0
    for j in sum_odds:
        sum = sum_odd(lambda j: j + sum, sum + j)
    print("Their sum is {}".format(sum))


number = int(input("Enter the length of the list > "))
data = []
if number > 0:
    data = fill_list(number)
    odd_sum(data)
else:
    print("The length should be positive.")
