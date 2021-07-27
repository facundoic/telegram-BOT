import logging
import telegram
from telegram.ext import Updater, CommandHandler
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv("TOKEN")


def start(update, context):
    name = update.message.from_user.username
    update.message.reply_text("Hi {} , welcome".format(name))


def main():
    updater = Updater(token)
    updater.dispatcher.add_handler(CommandHandler("start", start))

    # Start
    updater.start_polling()

    # Waiting
    updater.idle()


main()
