from handlers import bot 

with open("/home/pi/log.txt", 'a') as f:
    f.write("import handler.bot done \n")

def main():
    print("bot started")
    with open("/home/pi/log.txt", 'a') as f:
        f.write("bot started \n")
    bot.polling(none_stop=True)

if __name__ == "__main__":
    main()