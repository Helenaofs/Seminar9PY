from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_command import *


app = ApplicationBuilder().token("ВАШ ТОКЕН ПЛИЗ").build()       

app.add_handler(CommandHandler("start", hello_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("calc", calc_command))
app.add_handler(CommandHandler("sum", sum_command))
app.add_handler(CommandHandler("sub", sub_command))
app.add_handler(CommandHandler("mult", mult_command))
app.add_handler(CommandHandler("div", div_command))
app.add_handler(CommandHandler("expo", expo_command))


print('start server')

app.run_polling()
