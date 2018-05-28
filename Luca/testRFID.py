#!/usr/bin/env python
import RPi.GPIO as GPIO
import signal
import time
import sys
import config

from pirc522 import RFID

class RFIDTest:
    def run(self):
        GPIO.setmode(GPIO.BOARD)
        self.rdr = RFID()
        self.util = self.rdr.util()
        self.util.debug = True
        while True:
            self.rdr.wait_for_tag()
            # print("no")
            (error, data) = self.rdr.request()
            if not error:
                print("\nDetected: " + format(data, "02x"))

            (error, uid) = self.rdr.anticoll()
            if not error:
                esa0 = hex(uid[0])
                esa1 = hex(uid[1])
                esa2 = hex(uid[2])
                esa3 = hex(uid[3])
                # esa = esa[2:10]
                print(esa0, esa1, esa2, esa3)


