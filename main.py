import string
import random

import telebot

bot = telebot.TeleBot('5169740021:AAFaRkiaM5yCnIWYwbu78GOfiyvPR0RTUeI')


def generate_random_string(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Pikabu":
        bot.send_message(message.from_user.id, "Привет с Пикабу! \nТвой код в Стиме: {}".format(generate_random_string(12)))
    elif message.text == "/start":
        bot.send_message(message.from_user.id,
                         "Привет! Я бот игры Alone in Nightmares.\nЯ могу помочь тебе разобраться в основах игры.\nТакже не забывай заходить в нашу группу в ВК:\nhttps://vk.com/alone_in_nightmares")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


bot.polling(none_stop=True, interval=0)
