from telebot import TeleBot

bot = TeleBot(token='7688992831:AAFB6AHFFH42-WWA9YXVpuBGz4T3GaP07UY')

@bot.message_handler(commands=['start'])
def wake_up(message):
    print(message)  # Выводим на печать объект message: посмотрим, что там внутри.
    chat = message.chat
    chat_id = chat.id
    bot.send_message(chat_id=chat_id, text='Спасибо, что включили меня')


@bot.message_handler(content_types=['text'])
def say_hi(message):
    chat = message.chat
    chat_id = chat.id
    bot.send_message(chat_id=chat_id, text='Привет, я KittyBot!')


bot.polling() 