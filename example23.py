# Нужно написать программу, которая сгенерирует трёхзначное случайное число и определит первую цифру, вторую и третью.

import random


def print_digits():
    number = random.randint(100, 999)
    print(number)

    number3 = number % 10
    number2 = number // 10 % 10
    number1 = number // 100

    print("The first digit is {}.".format(number1))
    print("The second digit is {}.".format(number2))
    print("The third digit is {}.".format(number3))


print_digits()
