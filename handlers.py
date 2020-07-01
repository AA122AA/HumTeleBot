from loader import bot
import HumTemp

@bot.message_handler(content_types=['text'])
def sendTemp(message):
    if message.text == "температура":
        m = HumTemp.measure()
        bot.send_message(message.chat.id, m.get('temp'))
    else:
        bot.send_message(message.chat.id, "upsss...")