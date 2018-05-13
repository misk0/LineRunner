import RPi.GPIO as GPIO
import time
import SimpleMFRC522
import config
from pirc522 import RFID


class RFIDReader:
    def __init__(self):
        self._running = True
        self.rdr = RFID()
        self.util = self.rdr.util()
        self.util.debug = True

    def terminate(self):
        self._running = False

    def identify_obstacle(self, uid):
        # shift last 4 digits in inverse order
        match = str(hex(uid[0]))[2:4] + str(hex(uid[1]))[2:4] + str(hex(uid[2]))[2:4] + str(hex(uid[3]))[2:4]
        print(match)
        if not config.inside_obstacle:
            if match in config.obstacle_start:
                print("Found ", config.obstacle_start.index(match))
                config.obstacle_number = config.obstacle_start.index(match)
                # config.inside_obstacle = True
        else:
            for quad in config.obstacle_end:
                if match in quad:
                    config.obstacle_number = config.obstacle_end.index(quad)
                    config.inside_obstacle = False

    def run(self):
        try:
            while self._running:
                self.rdr.wait_for_tag()
                (error, data) = self.rdr.request()
                # if not error:
                #     print("\nDetected: " + format(data, "02x"))

                (error, uid) = self.rdr.anticoll()
                if not error:
                    # print(uid)
                    self.identify_obstacle(uid)
                    #time.sleep(0.2)
        finally:
            a = 1
            # GPIO.cleanup()