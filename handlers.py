from loader import bot
from telebot import types
import HumTemp

markup = types.ReplyKeyboardMarkup()
markup.row('temperature', 'humidity')
markup.row('all info')

@bot.message_handler(content_types=['text'])
def sendTemp(message):
    m = HumTemp.measure()
    if message.text == "temperature":
        bot.send_message(message.chat.id, m.get('temp'))
    elif message.text == "humidity":
        bot.send_message(message.chat.id, m.get('hum'))
    elif message.text == "all info":
        bot.send_message(message.chat.id, m.items())
    else:
        bot.send_message(message.chat.id, "upsss...", reply_markup=markup)