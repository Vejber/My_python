# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и
# записать в файл многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import *


def polinom(n):
    polinom = ''
    for i in range(n+1):
        if i == 0:
            polinom += str(randint(1, n)) + '*x**' + str(n-i)
        elif i == n:
            polinom += '+' + str(randint(1, n))
        else:
            polinom += '+' + str(randint(1, n)) + '*x**'+str(n-i)
    return polinom


n = int(input("Enter a number > "))
with open('polimom.txt', 'a') as data:
    data.write(polinom(n))
