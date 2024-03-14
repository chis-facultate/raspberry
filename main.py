from sense_hat import SenseHat
from datetime import datetime
import time

sense = SenseHat()


def get_sense_data():
    return [sense.get_temperature(), sense.get_pressure(), sense.get_humidity(), datetime.now()]


if __name__ == '__main__':
    while True:
        print(get_sense_data())
        time.sleep(5)
