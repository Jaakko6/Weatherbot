#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Telegram bot for determine current weather at certain city.
For determine weather using OpenWeatherMap API.
Wrapper telegram bot is python-telegram-bot (https://github.com/python-telegram-bot)
"""
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import logging
import pyowm
import os


TOKEN = "1467684613:AAHWJ-ire79YU1yoweOMW8KOfjHsoqwAnjU"
OWM_KEY = "5d58dc1c25402358025e67224f8a56b2"
PORT = int(os.environ.get("PORT", 8443))

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def start(update: Update, context: CallbackContext):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi! I can determine current weather at city.')

def help(update: Update, context: CallbackContext):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Just type, for example, /weather Moscow')

def error(update: Update, context: CallbackContext):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)

def weather(update: Update, context: CallbackContext, args):
    """Define weather at certain location"""
    owm = pyowm.OWM(OWM_KEY)
    text_location = "".join(str(x) for x in args)
    observation = owm.weather_at_place(text_location)
    w = observation.get_weather()
    humidity = w.get_humidity()
    wind = w.get_wind()
    temp = w.get_temperature('celsius')
    convert_temp = temp.get('temp')
    convert_wind = wind.get('speed')
    convert_humidity = humidity
    text_temp = str(convert_temp)
    text_wind = str(convert_wind)
    text_humidity = str(convert_humidity)
    update.message.reply_text("Temperature, celsius: {}".format(text_temp))
    update.message.reply_text("Wind speed, m/s: {}".format(text_wind))
    update.message.reply_text("Humidity, %: {}".format(text_humidity))

def main():
    """Start the bot."""
    # Create the EventHandler and pass it your bot's token.
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("weather", weather, pass_args=True))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_webhook(listen="0.0.0.0",
                          port=PORT,
                          url_path=TOKEN)
    updater.bot.set_webhook("https://obscure-forest-19016.herokuapp.com/" + TOKEN)
    updater.idle()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
   

if __name__ == '__main__':
    main()