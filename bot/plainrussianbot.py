
# -*- coding: utf-8 -*-
import sys
import os
from urllib.parse import urlencode
import requests
import os

from pprint import pformat, pprint
import logging
import json
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

PLAIN_URLPAT = 'http://api.plainrussian.ru/api/1.0/ru/measure/'
PLAIN_POSTPAT = 'http://api.plainrussian.ru/api/1.0/ru/measure/'

PLAINBOT_KEY = '../.key_plainbot'
logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.DEBUG)

logger = logging.getLogger(__name__)


def start(bot, update):
    update.message.reply_text(u"""
    Привет! Это бот для оценки текстов на простоту языка
    - /text [содержание сообщения] - выдаст сложность текста сообщения
    - /url [ссылка на веб-страницу] - выдаст сложность текста по ссылке
    - /start или /help повтор этого сообщения
    Проверка работает корректно только на текстах от 2-х предложений и от 10 слов.

    Вопросы можно задавать @ibegtin или на почту ibegtin@infoculture.ru
    Бот сделан на базе API https://plainrussian.ru
    """)


def write_response(data):
    text = u''
    text += u'Результаты:\n'
    text += u'- уровень: %s \n' % (data['indexes']['grade_SMOG'])
    text += u'- необходимое обучение (в годах): %.2f \n' % (float(data['indexes']['index_SMOG']))
    text += u'Статистика:\n'
    text += u'- знаков: %d \n' % (data['metrics']['chars'])
    text += u'- букв: %d \n' % (data['metrics']['letters'])
    text += u'- пробелов: %d \n' % (data['metrics']['spaces'])
    text += u'- слогов: %d \n' % (data['metrics']['n_syllabes'])
    text += u'- слов: %d \n' % (data['metrics']['n_words'])
    text += u'- предложений: %d \n' % (data['metrics']['n_sentences'])
    text += u'- слогов на слово: %.2f \n' % (data['metrics']['avg_syl'])
    text += u'- слов на предложение: %.2f \n' % (data['metrics']['avg_slen'])
    text += u'- сложных слов: %d \n' % (data['metrics']['n_complex_words'])
    text += u'- простых слов: %d \n' % (data['metrics']['n_simple_words'])
    return text

def gettext(bot, update):
    query = update['message']['text']
    clean_query = query.split(' ', 1)[-1].strip()
    res = requests.post(PLAIN_POSTPAT, data = {'text':clean_query})
    data = json.loads(res.text)
    update.message.reply_text(write_response(data))


def geturl(bot, update):
    guesses = []
    query = update['message']['text']
    clean_query = query.split(' ', 1)[-1].strip()
    res = requests.get(PLAIN_URLPAT, params = {'url': clean_query})
    data = json.loads(res.text)
    update.message.reply_text(write_response(data))


def getdocument(bot, update):
    update.message.reply_text("Received")
    document = update['message']['document']
    file_id = update.message.document.file_id
    newFile = bot.get_file(file_id)
    newFile.download(update.message.document.file_name)
    update.message.reply_text(str(document))
    s = '"C:\Program Files (x86)\LibreOffice 5\program\soffice.exe" --headless --convert-to %s %s' % ('txt', os.path.abspath(update.message.document.file_name))
    print(s)
    os.system(s)
    text = open(update.message.document.file_name.rsplit('.', 1)[0] + '.txt').read()
    clean_query = text
    res = requests.post(PLAIN_POSTPAT, data = {'text':clean_query})
    data = json.loads(res.text)
    update.message.reply_text(write_response(data))


def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))

def echo(bot, update):
    update.message.reply_text(update.message.text)

updater = Updater(open(PLAINBOT_KEY, 'r').read())
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', start))
updater.dispatcher.add_handler(CommandHandler('url', geturl))
updater.dispatcher.add_handler(CommandHandler('text', gettext))
updater.dispatcher.add_handler(MessageHandler(Filters.document, getdocument))
# log all errors
updater.dispatcher.add_error_handler(error)
updater.start_polling()
updater.idle()
