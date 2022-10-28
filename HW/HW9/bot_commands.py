from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from random import *
from logger import *
# from logger import *
# import datetime
# как сделать чтобы бот ждал и учитывал ответ пользователя


async def hello_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Hi {update.effective_user.first_name}')


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    candies = 2021
    count_player1 = 0
    count_bot = 0
    # player1 = input("What's your name? > ")
    first_move = randint(1, 1)
    if first_move == 1:
        while candies > 0:
            # n1 = int(  update.message.reply_text('How many candies will you take this time? > '))
            # кладем сообщение пользователя в переменную
            # update.message.reply_text(
            #     'How many candies will you take this time? > ')
            await update.message.reply_text('How many candies will you take this time? > ')
            await update.message.reply_text('?')

            # await update.message.reply_text
            await log_command(update, context)
            n1 = update.message.text
            items = n1.split()  # создаем список из сообщения, 1 элемента (n)
            print(items)
            # msg = str(msg)
            n1 = int(items[0])
            print(n1)
        while (n1 <= 0 or n1 > 28 or n1 > candies):
            update.message.reply_text(
                "The number of candies taken should be more than zero, less than 29 and less than the number of candies left")
            n1 = int(update.message.reply_text(
                'How many candies will you take this time? > '))
        if (n1 > 0 and n1 < 29 and n1 <= candies):
            candies = candies - n1
            count_player1 = count_player1 + n1
            update.message.reply_text("Candies left {}.".format(candies))
            if candies == 0:
                update.message.reply_text("You win! The total of your candies is {}.". format(
                    count_bot+count_player1))
              #    break

        n2 = randint(1, 28)
        if n2 > candies:
            n2 = randint(1, candies)

        candies = candies - n2
        count_bot = count_bot + n2
        update.message.reply_text("Bot took {}.".format(n2))
        update.message.reply_text("Candies left {}.".format(candies))
        if candies == 0:
            update.message.reply_text("Bot wins! The total of its' candies is {}.". format(
                count_bot+count_player1))
            # break
    else:
        while candies > 0:
            n2 = randint(1, 28)
            if n2 > candies:
                n2 = randint(1, candies)

            candies = candies - n2
            count_bot = count_bot + n2
            update.message.reply_text("Bot took {}.".format(n2))
            update.message.reply_text("Candies left {}.".format(candies))
            if candies == 0:
                update.message.reply_text("Bot wins! The total of its' candies is {}.". format(
                    count_bot+count_player1))
                # break

            n1 = int(update.message.reply_text(
                "How many candies will you take this time? > "))
            while (n1 <= 0 or n1 > 28 or n1 > candies):
                update.message.reply_text(
                    "The number of candies taken should be more than zero, less than 29 and less than the number of candies left")
                n1 = int(update.message.reply_text(
                    "How many candies will you take this time? > "))
            if (n1 > 0 and n1 < 29 and n1 <= candies):
                candies = candies - n1
                count_player1 = count_player1 + n1
                update.message.reply_text("Candies left {}.".format(candies))
                if candies == 0:
                    update.message.reply_text("You win! The total of your candies is {}.". format(
                        count_bot+count_player1))
                  # break
            update.message.reply_text(f'Hi {update.effective_user.first_name}')
