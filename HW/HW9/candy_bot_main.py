from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *
# from logger import *


# async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     await update.message.reply_text(f'Hello {update.effective_user.first_name}')


app = ApplicationBuilder().token(
    "5708923731:AAEyzEvexF8j_n4-DNK_Os72qx7GRO0q8dk").build()

# list of bot's commands:
app.add_handler(CommandHandler('hello', hello_command))
app.add_handler(CommandHandler('start', start_command))
# app.add_handler(CommandHandler('help', help_command))
# app.add_handler(CommandHandler('sum', sum_command))a
print('server start')

app.run_polling()
