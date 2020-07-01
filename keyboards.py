from telebot import types

def keyboard():
    markup = types.ReplyKeyboardMarkup()
    markup.row('temperature', 'humidity')
    markup.row('all info')
    return markup
