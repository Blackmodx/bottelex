import os
import logging
from telegram.ext import Updater, MessageHandler, CommandHandler, Filters

TOKEN = os.getenv('TELEGRAM_TOKEN')


def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def chat(s):
    return s


def handle_message(update, context):
    print("inside")
    tx = update.message.text
    re = chat(tx)
    update.message.reply_text(re)


def main():
    updater = Updater(token=TOKEN, use_context=True)
    dp = updater.dispatcher

    # dp.add_handler(CommandHandler(Filters.text, handle_message))
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


main()