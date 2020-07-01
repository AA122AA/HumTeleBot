from telebot import types

def create_keyboard():
    markup = types.ReplyKeyboardMarkup()
    markup.row('temperature', 'humidity')
    markup.row('all info')
    return markup
