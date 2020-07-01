import telebot
from config import TOKEN
from telebot import types

bot = telebot.TeleBot(TOKEN) 

def main():
    bot.polling(none_stop=True)

if __name__ == "__main__":
    main()