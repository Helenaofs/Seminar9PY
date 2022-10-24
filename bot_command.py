from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime
from log import *


async def hello_command(update: Update, context: ContextTypes):
    log(update, context)
    await update.message.reply_text(f'Привет, {update.effective_user.first_name}! Специально для тебя я приготовил список команд, которые я умею выполнять. Введи /help')


async def time_command(update: Update, context: ContextTypes):
    log(update, context)
    await update.message.reply_text(f'Хотите узнать который час? {datetime.datetime.now().time()}')


async def help_command(update: Update, context: ContextTypes):
    log(update, context)
    await update.message.reply_text(f'Функции, которые я могу реализовать\n/start\n/time\n/help\n/calc')


async def calc_command(update: Update, context: ContextTypes):
    log(update, context)
    await update.message.reply_text(f'/sum - сложение\n/sub - вычитание\n/mult - умножение\n/div - деление\n/expo - возведение в степень\nвведи выбранную команду и числа, над которыми хочешь произвести арифметическую операцию')


async def sum_command(update: Update, context: ContextTypes):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} + {y} = {x + y}')


async def sub_command(update: Update, context: ContextTypes):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} - {y} = {x - y}')


async def mult_command(update: Update, context: ContextTypes):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} * {y} = {x * y}')


async def div_command(update: Update, context: ContextTypes):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} / {y} = {x / y}')


async def expo_command(update: Update, context: ContextTypes):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} ** {y} = {x ** y}')
