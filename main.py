from pirc522 import RFID
import RPi.GPIO as GPIO
import signal
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(33, GPIO.OUT)
rdr = RFID()
util = rdr.util()
util.debug = True

while True:
    rdr.wait_for_tag()

    (error, data) = rdr.request()

    if not error:
        print("\nDetected")

        (error, uid) = rdr.anticoll()

        if not error:
            # Print UID
            print("Card read UID: " + str(uid[0]) + "," + str(uid[1]) + "," + str(uid[2]) + "," + str(uid[3]))
            util.set_tag(uid)
            util.auth(rdr.auth_b, [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF])
            util.read_out(10)
            util.read_out(11)
            util.rewrite(11, [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, None, None, None, None, None, None, None, None, None, None])

            GPIO.output(33, GPIO.HIGH)
            time.sleep(0.4)
            GPIO.output(33, GPIO.LOW)

        time.sleep(5)