from handlers import bot 

with open("/home/pi/log.txt", 'a') as f:
    f.write("import handler.bot done \n")

def main():
    print("bot started")
    with open("/home/pi/log.txt", 'a') as f:
        f.write("bot started \n")
    try:
        bot.polling(none_stop=True)     
    except ModuleNotFoundError as e:
        with open("/home/pi/log.txt", 'a') as f:
            f.write(e + "\n")
    except:
        with open("/home/pi/log.txt", 'a') as f:
            f.write("bot drop polling \n")
    
    with open("/home/pi/log.txt", 'a') as f:
       f.write("bot polling \n")

if __name__ == "__main__":
    main()