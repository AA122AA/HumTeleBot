try:
    import telebot
except ModuleNotFoundError as e:
    with open("/home/pi/error.txt", 'w') as f:
        f.write(e)
from data.config import TOKEN
from utils.db.db import init_db

init_db()
bot = telebot.TeleBot(TOKEN)