# Нужно собрать цикл, который 10 раз выведет на экран трёхзначное случайное число. 
# Все числа обязательно должны быть целыми, положительными и чётными.
# определить сумму этих чисел

import random

def tri_cycle_sum():
    count = 0
    sum = 0
    while(count < 11):
        number = random.randint(100, 999)
        print(number)
        sum = sum + number
        count = count + 1
    print(sum)

tri_cycle_sum()