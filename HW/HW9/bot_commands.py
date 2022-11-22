import telebot
from random import randint
import time
from pytube import *

bot = telebot.TeleBot(
    "5708923731:AAEyzEvexF8j_n4-DNK_Os72qx7GRO0q8dk", parse_mode=None)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hey!")


@bot.message_handler(func=lambda message: True)
def video_send(message):
    chat_id = message.chat.id
    yt = YouTube(message.text)
    yt.streams.filter(res="360p").first().download(filename=f"{chat_id}.mp4")
    bot.send.video(chat_id, video=open(
        f"{chat_id}.mp4", 'rb'), supports_streaming=True)
    print(yt.title)


bot.infinity_polling()
