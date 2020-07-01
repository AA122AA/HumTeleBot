import sys
import Adafruit_DHT

def measure():
    humidity, temperature = Adafruit_DHT.read_retry(11,4)
    d = dict(temp=str(temperature), hum=(str(humidity)))
    return d
