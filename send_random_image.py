import requests
from telebot import TeleBot


bot = TeleBot(token='7688992831:AAFB6AHFFH42-WWA9YXVpuBGz4T3GaP07UY')

URL = 'https://api.thecatapi.com/v1/images/search'

def send_random_cat():
    response = requests.get(URL).json()
    photo = response[0].get('url')
    return photo

@bot.message_handler(commands=['newcat'])
def new_cat(message):
    bot.send_photo(message.chat.id, send_random_cat())

@bot.message_handler(commands=['start'])
def wake_up(message):
    bot.send_photo(message.chat.id, send_random_cat())
    bot.send_message(message.chat.id, text=f'Привет, {message.from_user.first_name} посмотри какого котенка я тебе нашел')

bot.polling()