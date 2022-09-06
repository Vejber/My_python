# Нужно написать программу, которая запрашивает у пользователя три целых числа и выводит наибольшее из них.
number_1 = int(input("Введите первое число > "))
number_2 = int(input("Введите второе число > "))
number_3 = int(input("Введите третье число > "))
max = number_1
if number_2 > max:
    max = number_2
if number_3 > max:
    max = number_3
print(max)