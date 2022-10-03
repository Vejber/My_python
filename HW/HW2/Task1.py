# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# *Пример:*

# - 6782 -> 23
# - 0,56 -> 11

def sum_digits(list):
    result = 0
    for i in range(len(list)):
        if (list[i] == '.' or list[i] == '-'):
            continue
        else:
            result = result + int(list[i])
    print(result)

number = list(input("Enter your number > "))
print (number)
sum_digits(number)

