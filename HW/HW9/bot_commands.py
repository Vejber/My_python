import telebot
from random import randint

bot = telebot.TeleBot(
    "5708923731:AAEyzEvexF8j_n4-DNK_Os72qx7GRO0q8dk", parse_mode=None)

# is_game_on = False
# candies = 2021


def bots_move(message):
    global candies, is_game_on
    n = randint(1, 28)
    if n < candies:
        candies -= n
        bot.send_message(
            message.chat.id, f'Bot took {n} candies. The number of candies left is {candies}.')
    else:
        is_game_on = False
        bot.send_message(message.chat.id, 'Game over. Bot wins.')


@bot.message_handler(commands=['start'])
def start_game(message):
    global is_game_on
    if not is_game_on:
        global candies
        is_game_on = True
        is_players_turn = bool(randint(0, 1))
        bot.send_message(
            message.chat.id, f'The number of candies left is {candies}. {"Player" if is_players_turn else "Bot"} does the first move')
        bot.send_message(
            message.chat.id, 'Enter a number less than 29.') if is_players_turn else bots_move(message)
        if is_game_on:
            is_players_turn = not is_players_turn


@bot.message_handler(func=lambda _: is_game_on)
def players_move(message):
    global candies, is_game_on
    try:
        n = int(message.text)
        if n > 28:
            bot.send_message(
                message.chat.id, 'The number should not be more than 28. Try again.')
        else:
            if n < candies:
                candies -= n
                bot.send_message(
                    message.chat.id, f'The number of candies left is {candies}.')
                bots_move(message)
                if is_game_on:
                    bot.send_message(
                        message.chat.id, 'Enter a number less than 29.')
            else:
                candies = 0
                is_game_on = False
                bot.send_message(message.chat.id, 'The game is over, you win.')
    except:
        bot.send_message(message.chat.id, 'Try again.')


bot.infinity_polling()
