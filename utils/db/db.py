import sqlite3

#Декоратор для безопасного подключения к базе данных
def ensure_connection(func):
    def inner(*args, **kwargs):
        with sqlite3.connect('/home/pi/GitHub/HumTeleBot/utils/db/tempHumData.db') as conn:
            print("connection success")
            kwargs['conn'] = conn
            res = func(*args, **kwargs)
        return res

    return inner

#Проверить что нужные таблицы существуют, иначе создать их
@ensure_connection
def init_db(conn, force: bool = False): #force - пересоздание таблицы 
    c = conn.cursor()
    if force:
        c.execute('DROP TABLE IF EXISTS temp_hum_data')
    
    creat_table = """CREATE TABLE IF NOT EXISTS temp_hum_data (
                        id          INTEGER PRIMARY KEY,
                        Time        text NOT NULL,
                        Temperature text NOT NULL,
                        Humidity    ext NOT NULL

                    );"""     
    c.execute(creat_table)
    # Сохранить изменения
    conn.commit()
    print("db created or allready exists")

@ensure_connection
def add_data(conn, time: str, temp: str, hum: str):
    c = conn.cursor()
    c.execute('INSERT INTO temp_hum_data (Time, Temperature, Humidity) VALUES(?,?,?)', (time, temp, hum))
    conn.commit()
