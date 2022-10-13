# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# person/bot:
from random import *

candies = 2021
count_player1 = 0
count_bot = 0
player1 = input("What's your name? > ")
first_move = randint(1, 2)
if first_move == 1:
    while candies > 0:
        n1 = int(
            input("{}, how many candies will you take this time? > ". format(player1)))
        while (n1 <= 0 or n1 > 28 or n1 > candies):
            print("The number of candies taken should be more than zero, less than 29 and less than the number of candies left")
            n1 = int(
                input("{}, how many candies will you take this time? > ". format(player1)))
        if (n1 > 0 and n1 < 29 and n1 <= candies):
            candies = candies - n1
            count_player1 = count_player1 + n1
            print("Candies left {}.".format(candies))
            if candies == 0:
                print("{}, you win! The total of your candies is {}.". format(
                    player1, count_bot+count_player1))
                break

        n2 = randint(1, 28)
        if n2 > candies:
            n2 = randint(1, candies)

        candies = candies - n2
        count_bot = count_bot + n2
        print("Bot took {}.".format(n2))
        print("Candies left {}.".format(candies))
        if candies == 0:
            print("Bot, you win! The total of your candies is {}.". format(
                count_bot+count_player1))
            break
else:
    while candies > 0:
        n2 = randint(1, 28)
        if n2 > candies:
            n2 = randint(1, candies)

        candies = candies - n2
        count_bot = count_bot + n2
        print("Bot took {}.".format(n2))
        print("Candies left {}.".format(candies))
        if candies == 0:
            print("Bot, you win! The total of your candies is {}.". format(
                count_bot+count_player1))
            break

        n1 = int(
            input("{}, how many candies will you take this time? > ". format(player1)))
        while (n1 <= 0 or n1 > 28 or n1 > candies):
            print("The number of candies taken should be more than zero, less than 29 and less than the number of candies left")
            n1 = int(
                input("{}, how many candies will you take this time? > ". format(player1)))
        if (n1 > 0 and n1 < 29 and n1 <= candies):
            candies = candies - n1
            count_player1 = count_player1 + n1
            print("Candies left {}.".format(candies))
            if candies == 0:
                print("{}, you win! The total of your candies is {}.". format(
                    player1, count_bot+count_player1))
                break
