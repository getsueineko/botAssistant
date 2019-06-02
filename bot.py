# !python3
# !/usr/bin/python3
# -*- coding: utf-8 -*-

import config
import telebot
#from telebot import apihelper
from telebot import types
from emoji import emojize

#apihelper.proxy = config.proxy
bot = telebot.TeleBot(config.token)

smiley = emojize(":smiley:", use_aliases=True)
imp = emojize(":imp:", use_aliases=True)
pensive = emojize(":pensive:", use_aliases=True)

class Responser():
    delimiter = ' '

    def __init__(self, config, default):
        self.config = config
        self.default = default
        self.cache = {}
        self._load_config(config)

    def _load_config(self, config):
        # CACHE tuple with all the words
        for section, data in self.config.items():
            for w in data.get('markers', []):
                if w not in self.cache:
                    self.cache[w] = section

    def get_message(self, input):
        # IN Cache?
        index = self.default
        for word in input.split(self.delimiter):
            if self.cache.get(word):
                index = self.cache[word]
                break
        return self.config[index]['message']


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    if message.chat.id in config.userid:
        bot.send_message(message.chat.id, "Привет, " + config.userid[message.chat.id])
        start_keyboard(message)
    else:
        bot.send_message(message.chat.id, "Привет. К сожалению, я не знаю тебя, " + imp + " и следовательно "
                                                                    "не смогу помочь. Но мы можем поболтать.")


def start_keyboard(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("Напомнить PIN-код к Pritunl")
    markup.add("Получить OVPN-профайл")
    markup.add("Получить ссылку для Outline")
    bot.send_message(message.chat.id,
                     "Небольшой склероз? У меня есть правильные ноотропы " + smiley,
                     reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "Напомнить PIN-код к Pritunl")
def get_pritunl(message):
    if all([(message.text == "Напомнить PIN-код к Pritunl"), (message.chat.id in config.userid)]):
        bot.send_message(message.chat.id, config.pritunlInfo[message.chat.id])


@bot.message_handler(func=lambda message: message.text == "Получить OVPN-профайл")
def get_ovpn(message):
    if all([(message.text == "Получить OVPN-профайл"), (message.chat.id in config.userid)]):
        alias = config.pritunlInfo[message.chat.id]
        alias = alias[:6]
        filename = 'certs/2w1ftc-cz_' + alias + '_ensis.ovpn'
        bot.send_document(message.chat.id, open(filename, 'rb'))


@bot.message_handler(func=lambda message: message.text == "Получить ссылку для Outline")
def get_link(message):
    if all([(message.text == "Получить ссылку для Outline"), (message.chat.id in config.userid)]):
        bot.send_message(message.chat.id, config.outlineLink[message.chat.id])


# default handler for every other text
@bot.message_handler(func=lambda message: True, content_types=['text'])
def command_default(m):
    # this is the standard reply to a normal message
    i = m.text.lower()
    r = Responser(config.RESPONSES, config.DEFAULT)
    bot.send_message(m.chat.id, r.get_message(i))


bot.polling(none_stop=True)
