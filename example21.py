# Нужно собрать цикл, который 10 раз выведет на экран трёхзначное случайное число. 
# Все числа обязательно должны быть целыми, положительными и чётными.

import random

def tri_cycle():
    count = 0;
    while(count < 11):
        number = random.randint(100, 999)
        print(number)
        count = count + 1

tri_cycle()