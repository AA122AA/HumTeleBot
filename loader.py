import telebot
from data.config import TOKEN
from utils.db.db import init_db

init_db()
bot = telebot.TeleBot(TOKEN)