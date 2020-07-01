from loader import bot
from keyboards import keyboard
from utils import HumTemp
from utils.db.db import add_data
import time

@bot.message_handler(content_types=['text'])
def sendTemp(message):
    markup = keyboard.create_keyboard()
    m = HumTemp.measure()
    add_data(time=time.ctime(), temp=m.get('temp'), hum=m.get('hum'))
    if message.text == "temperature":
        text = "temperature - " + m.get('temp') + "C"
        bot.send_message(message.chat.id, text)
    elif message.text == "humidity":
        text = "humidity - " + m.get('hum') + "%"
        bot.send_message(message.chat.id, text)
    elif message.text == "all info":
        text = "temperature - " + m.get('temp')  + "C" + "\n" + "humidity - " + m.get('hum') + "%"
        bot.send_message(message.chat.id, text)
    else:
        bot.send_message(message.chat.id, 
                        "I can only send you temp and hum. Please click button.", 
                        reply_markup=markup)