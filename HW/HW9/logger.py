from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def log_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file = open('HW/HW9/logger.csv', 'w')
    file.write(
        f'{update.message.text}\n')
    file.close()
