import RPi.GPIO as GPIO
import config
from time import sleep

class FollowMeBaby:
    def __init__(self):
        self._running = True
        # GPIO.setmode(GPIO.BOARD)

        self.pin = [38, 33, 36, 35, 37]
        # pin[0]: sensore esterno destra     //Nello schizzo S4
        # pin[4]: sensore interno destra     //Nello schizzo S2
        # pin[1]: sensore esterno sinistra   //Nello schizzo S5
        # pin[3]: sensore interno sinistra   //Nello schizzo S3
        # pin[2]: sensore centrale           //Nello schizzo S1
        # pin[5]: sensore centrale arretrato //Nello schizzo S6
        i = 0
        while i < 5:
            GPIO.setup(self.pin[i], GPIO.IN)  # Assegnazione valore numerico ai pin sui quali verrà letto l'input
            i = i + 1

    def terminate(self):
        self._running = False


    def run(self):
        try:
            while True:
                i = 0
                while i < 5:
                    i += 1
                    if GPIO.input(self.pin[i]) == 1:
                        print("PIN {} black".format(i))

                # # Va' capito se è possibile che sul pin[2] e sul pin[3] (o sul pin[2] e sul pin[4]) venga letto nero in contemporanea
                # # v motore sinistro < v motore destro
                # if GPIO.input(self.pin[3]) == 0 and GPIO.input(self.pin[2]) == 1 or GPIO.input(self.pin[3]) == 0 and GPIO.input(
                #         self.pin[2]) == 0:
                #     print("v motore sinistro < v motore destro")
                #     while GPIO.input(pin[2]) == 1:
                #         left_motor_speed = left_motor_speed - 0.05

                # # v motore sinistro > v motore destro
                # if GPIO.input(self.pin[4]) == 0 and GPIO.input(self.pin[2]) == 1 or GPIO.input(self.pin[4]) == 0 and GPIO.input(
                #         self.pin[2]) == 0:
                #     print("# v motore sinistro > v motore destro")
                #     while GPIO.input(pin[2]) == 1:
                #         right_motor_speed = right_motor_speed - 0.05
                #
                # # fermare i motori
                # # -1*(v motore destro) = v motore sinistro
                # if GPIO.input(self.pin[2]) == 1 and GPIO.input(self.pin[3]) == 1 and GPIO.input(self.pin[4]) == 0:
                #     print("-1*(v motore destro) = v motore sinistro")
                #
                # # fermare i motori
                # # -1*(v motore sinistro) = v motore destro
                # if GPIO.input(self.pin[2]) == 1 and GPIO.input(self.pin[3]) == 1:
                #     print("-1*(v motore sinistro) = v motore destro")
                #
                # # v motore destro = v motore sinistro
                # if GPIO.input(self.pin[2]) == 0:  # Se legge nero
                #     print("v motore destro = v motore sinistro")
        finally:
            GPIO.cleanup()
