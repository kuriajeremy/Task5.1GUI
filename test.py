# Code for Raspberry Pi testing

import RPi.GPIO as GPIO
import time

# setting up the pins using BCM numbering
GPIO.setmode(GPIO.BCM)

# assign GPIO pins to each room LED
living_room = 14
bathroom    = 15
closet      = 16

# setting all pins as output
GPIO.setup(living_room, GPIO.OUT)
GPIO.setup(bathroom,    GPIO.OUT)
GPIO.setup(closet,      GPIO.OUT)

# function to turn all lights off (helper function)
def turn_off_all():
    GPIO.output(living_room, GPIO.LOW)
    GPIO.output(bathroom,    GPIO.LOW)
    GPIO.output(closet,      GPIO.LOW)

# main loop for continuous testing
try:
    while True:
        # living room light on
        turn_off_all()
        GPIO.output(living_room, GPIO.HIGH)
        time.sleep(2)

        # bathroom light on
        turn_off_all()
        GPIO.output(bathroom, GPIO.HIGH)
        time.sleep(2)

        # closet light on
        turn_off_all()
        GPIO.output(closet, GPIO.HIGH)
        time.sleep(2)

        # all lights off before repeating
        turn_off_all()
        time.sleep(4)

#stops the program manually
except KeyboardInterrupt:
    turn_off_all()       # all LEDs are off
    GPIO.cleanup()       # releases the GPIO pins
    print("Program stopped properly.")
