"""
Telegram weather bot
"""

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import pyowm
import os

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

TOKEN = "1467684613:AAHWJ-ire79YU1yoweOMW8KOfjHsoqwAnjU"
PORT = int(os.environ.get("PORT", 8443))

def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hei, minkä kaupungin sään haluat tietää?')

def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Kirjoita kaupungin nimi, esim. /weather Turku')

def error(update, error, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def weather(update, args):
    """Define weather at certain location"""
    owm = pyowm.OWM('dd5185db8471b85647e7626571b85db8')
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
    update.message.reply_text("Lämpötila, celsius: {}".format(text_temp))
    update.message.reply_text("Tuulen nopeus, m/s: {}".format(text_wind))
    update.message.reply_text("Kosteus, %: {}".format(text_humidity))

def main():
    """Start the bot."""

    updater = Updater(TOKEN, use_context=True)
    # Create the EventHandler and pass it your bot's token.
    #updater = Updater(TOKEN)

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
    # updater.bot.set_webhook(url=settings.WEBHOOK_URL)
    updater.bot.set_webhook("https://obscure-forest-19016.herokuapp.com/"  + TOKEN)
    updater.idle()


if __name__ == '__main__':
    main()