# Weatherbot

This is my first time I tried to code a Telegram bot. It is supposed to show few basic weather elements as temperature, relative humidity and wind speed to the user.
The bot is written in Python and uses Telegram ext. package. I found out that there are many different ways to write even a simple code for a Telegram bot, but I chose to pick a couple of existing codes and examples and then started to write a code of my own. I'm using Heroku webhook to deploy my app, because it can be run anytime regardless of my editor being closed.

The bot starts to communicate when you send a message: "/start". Ths is one of the basic commands used in the library. The bot then asks the city of which wetather you would like to know and you just write "/City", and it gives the weather in a plain text format. At the time the weather function does not work like it should, but it is under debugging.

Don't mind about those commits on files Procfile and requirement.txt, they are being updated as well...
