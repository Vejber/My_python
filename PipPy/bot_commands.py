from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from logger import *
import datetime


async def hello_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log_command(update, context)
    await update.message.reply_text(f'Hi {update.effective_user.first_name}')


async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log_command(update, context)
    await update.message.reply_text(f'{datetime.datetime.now().time()}')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log_command(update, context)
    await update.message.reply_text(f'/hello\n/time\n/sum\n/help')


async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log_command(update, context)
    msg = update.message.text  # кладем сообщение пользователя в переменную
    items = msg.split()  # создаем список из сообщения, 3 элемента (/sum, 123, 456)
    x = int(items[1])
    y = int(items[2])

    await update.message.reply_text(f'{x} + {y} = {x+y}')
