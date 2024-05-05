from telegram.ext import Updater, CommandHandler, MessageHandler, filters
from telegram import Bot
import requests


def start(update, context):
    update.message.reply_text("Hello! I'm a weather forecast bot. Just send me the name of the city, i will give you the current weather forecast.")


def weather(update, context):
    city = update.message.text
    api_key = 'ed21c96d8304b0d6173019d380045c02'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        update.message.reply_text(f'The weather in city {city}: {weather_description}, temperature: {temperature}°C')
    else:
        update.message.reply_text('Failed to get weather forecast. Please try again.')

def main():
    TOKEN = '6744084768:AAGh-4fkCkXxHW_9ZgPuofsrKkIgg5eGSUA'  
    bot = Bot(token=TOKEN)
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(filters.text & ~filters.command, weather))
    updater.start_polling()