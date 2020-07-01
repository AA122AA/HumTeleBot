from loader import bot
from keyboards import keyboard
import HumTemp

markup = keyboard
@bot.message_handler(content_types=['text'])
def sendTemp(message):
    m = HumTemp.measure()
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