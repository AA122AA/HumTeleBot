import telebot

with open("/home/pi/stop.txt", 'w') as f:
    f.write("import done")
from data.config import TOKEN
from utils.db.db import init_db

init_db()
bot = telebot.TeleBot(TOKEN)