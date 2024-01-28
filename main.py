import telebot
import types
import time
from photos import *
from texts import *
from buttons import (
FIRST_QUESTION,
SECOND_QUESTION,
THERD_QUESTION,
FORTH_QUESTION,
FIFTH_QUESTION,
SIXTH_QUESTION
)
bot = telebot.TeleBot(token="6553315261:AAEF4XgfDKBW46LTuwZUA6wXaKcQVifYGdY")

all_right = ""

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Добро пожаловать, это бот с помощью которого можно закрепить свои знания о планетах")
    bot.send_message(message.chat.id, "Напишите /starting для начала")

@bot.message_handler(commands=["starting"])
def starting(message):
    bot.send_photo(message.chat.id, photo=photo1, caption=text1, reply_markup=FIRST_QUESTION)

@bot.callback_query_handler(func=lambda call: call.data == "wrong")
def text_wrong(call):
    bot.send_message(call.message.chat.id, "Попробуй еще раз, напиши /starting чтобы продолжить")


@bot.callback_query_handler(func=lambda call: call.data == "earth_correct")
def earth_cor(call):
    bot.send_message(call.message.chat.id, "Моледец правильно")
    bot.send_photo(call.message.chat.id, photo=photo2, caption=text1, reply_markup=SECOND_QUESTION)

@bot.callback_query_handler(func=lambda call: call.data == "upiter_correct")
def upiter_cor(call):
    bot.send_message(call.message.chat.id, "Моледец правильно")
    bot.send_photo(call.message.chat.id, photo=photo3, caption=text1, reply_markup=THERD_QUESTION)

@bot.callback_query_handler(func=lambda call: call.data == "mercury_correct")
def mercury_cor(call):
    bot.send_message(call.message.chat.id, "Моледец правильно")
    bot.send_photo(call.message.chat.id, photo=photo4, caption=text1, reply_markup=FORTH_QUESTION)

@bot.callback_query_handler(func=lambda call: call.data == "saturn_correct")
def saturn_corr(call):
    bot.send_message(call.message.chat.id, "Умничка")
    bot.send_photo(call.message.chat.id, photo=photo5, caption=text1, reply_markup=FIFTH_QUESTION)

@bot.callback_query_handler(func=lambda call: call.data == "neptun_correct")
def neptun_corr(call):
    bot.send_message(call.message.chat.id, "У тебя здорово получается")
    bot.send_photo(call.message.chat.id, photo=photo6, caption=text1, reply_markup=SIXTH_QUESTION)

@bot.callback_query_handler(func=lambda call: call.data == "mars_correct")
def mars_corr(call):
    bot.send_message(call.message.chat.id, "Молодец, ты знаешь ответы на все вопросы. Отправь друзьям, чтобы тоже знали название всех планет")

bot.infinity_polling()
