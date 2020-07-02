from handlers import bot 

def main():
    print("bot started")
    bot.polling(none_stop=True)      

if __name__ == "__main__":
    main()