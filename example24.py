# Нужно написать программу, которая сгенерирует случайное дробное число и определит первую цифру после точки.

import random

def digit_after_point():
    number = random.triangular(1, 5)
    print (number)
    number = int((number * 10) % 10)
    print("The first digit after the point in the number is {}.". format(number))

digit_after_point()