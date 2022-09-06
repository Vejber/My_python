# Нужно написать программу, которая запрашивает у пользователя три целых числа и выводит наименьшее из них.

number_1 = int(input("Введите первое число > "))
number_2 = int(input("Введите второе число > "))
number_3 = int(input("Введите третье число > "))
min = number_1
if number_2 < min:
    min = number_2
elif number_3 < min:
    min = number_3
print(min)