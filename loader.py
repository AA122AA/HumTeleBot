import telebot

with open("/home/pi/stop.txt", 'w') as f:
    f.write("import telebot done \n")
from data.config import TOKEN
from utils.db.db import init_db

with open("/home/pi/stop.txt", 'w') as f:
    f.write("import Token and init_db done \n")

init_db()
with open("/home/pi/stop.txt", 'w') as f:
    f.write("init_db done \n")
bot = telebot.TeleBot(TOKEN)