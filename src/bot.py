import logging
import telegram
from telegram.ext import Updater, CommandHandler
from dotenv import load_dotenv
import os
from datetime import date, datetime

load_dotenv()
token = os.getenv("TOKEN")
path_images = os.getenv("PATH_IMAGES")

now = datetime.now()
time_now = now.strftime("%d/%m/%y %H:%M")


def start(update, context):
    name = update.message.from_user.username
    update.message.reply_text("Hi {} , welcome".format(name))


def camera1(update, context):
    image1 = path_images + 'camera1.jpg'
    update.message.bot.send_photo(
        update.message.chat.id, open(image1, 'rb'))
    update.message.reply_text("the time of the photo is : {}".format(time_now))


def camera2(update, context):
    image2 = path_images + 'camera2.jpg'
    update.message.bot.send_photo(
        update.message.chat.id, open(image2, 'rb'))
    update.message.reply_text("the time of the photo is : {}".format(time_now))


def camera3(update, context):
    image3 = path_images + 'camera3.jpg'
    update.message.bot.send_photo(
        update.message.chat.id, open(image3, 'rb'))
    update.message.reply_text("the time of the photo is : {}".format(time_now))


def camera4(update, context):
    image4 = path_images + 'camera4.jpg'
    update.message.bot.send_photo(
        update.message.chat.id, open(image4, 'rb'))
    update.message.reply_text("the time of the photo is : {}".format(time_now))


def main():
    updater = Updater(token)
    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(CommandHandler("camera1", camera1))
    updater.dispatcher.add_handler(CommandHandler("camera2", camera2))
    updater.dispatcher.add_handler(CommandHandler("camera3", camera3))
    updater.dispatcher.add_handler(CommandHandler("camera4", camera4))

    # Start
    updater.start_polling()
    print("The bot started successfully ")
    # Waiting
    updater.idle()


main()
