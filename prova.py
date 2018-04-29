import RPi.GPIO as GPIO
import config
from time import sleep

GPIO.setmode(GPIO.BOARD)

pin = [38, 33, 36, 35, 37]
        # pin[0]: sensore esterno destra     //Nello schizzo S4
        # pin[4]: sensore interno destra     //Nello schizzo S2
        # pin[1]: sensore esterno sinistra   //Nello schizzo S5
        # pin[3]: sensore interno sinistra   //Nello schizzo S3
        # pin[2]: sensore centrale           //Nello schizzo S1
        # pin[5]: sensore centrale arretrato //Nello schizzo S6
i = 0
while i < 5:
    GPIO.setup(pin[i], GPIO.IN)  # Assegnazione valore numerico ai pin sui quali verrà letto l'input
    i = i + 1

print("Starting")
while True:
    i = 0
    while i < 5:
        if GPIO.input(pin[i]) == 1:
            print("PIN {} black".format(i))
        i += 1

GPIO.cleanup()
