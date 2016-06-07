#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Bot para o Telegram que traduz de português para portunhol, baseado no
# código de Tiago Queiroz, com contribuições de Yumi e Anchises, criado
# durante a Virada Hacker 2016, no Garoa Hacker Clube.

'''
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
from portunhol.portunhol import conbertir_frasses_cumplietas

# Enable logging
logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO)

logger = logging.getLogger(__name__)

# Define alguns command handlers. Geralmente pegam dois argumentos, bot e
# update. Error handlers também recebem o objeto de erro TelegramError.
def start(bot, update):
    pass

def help(bot, update):
    mensagem = 'Envie uma mensagem, que o Miguelito a repete para você!'
    bot.sendMessage(update.message.chat_id, text=mensagem)

def echo(bot, update):
    texto = update.message.text
    final = conbertir_frasses_cumplietas(texto)
    bot.sendMessage(update.message.chat_id, text=final)

def error(bot, update, error):
    logger.warn('Atualização "%s" causou o erro "%s"' % (update, error))

def main():
    # Create the EventHandler and pass it your bot's token.
    updater = Updater('180259485:AAH4hNkCqqc_2nHVpp2FXW0A1NoIc8BLuU8')

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler('start', help))
    dp.add_handler(CommandHandler('help', help))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler([Filters.text], echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until the you presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()
