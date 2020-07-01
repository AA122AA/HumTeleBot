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
        bot.send_message(message.chat.id, "temperature - " + m.get('temp'))
    elif message.text == "humidity":
        bot.send_message(message.chat.id, "humidity - " + m.get('hum'))
    elif message.text == "all info":
        text = "temperature - " + m.get('temp') + "\n" + "humidity - " + m.get('hum')
        bot.send_message(message.chat.id, text)
    else:
        bot.send_message(message.chat.id, "I can only send you temp and hum. Please click button.", reply_markup=markup)