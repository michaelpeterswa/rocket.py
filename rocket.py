# michaelpeterswa
# rocket.py
# 02.21.21

# import Raspberry Pi GPIO module
import RPi.GPIO as GPIO
import time

def setup():

    # Initialize pinout
    GPIO.setmode(GPIO.board)

    # Set pins
    accel = None # accelerometer pin
    servo = None # servo pin

    GPIO.setup(accel, GPIO.IN)
    GPIO.setup(servo, GPIO.OUT)

do_math():
    print("doing math")

end():
    print("cleaning up")

def main():
    init_time = time.time()
    burnout_time = 10 # time in seconds
    launched = False

    acceleration = 0
    acceleration = 10

    if acceleration > 1 and not launched:
        launched = True

    if launched:
        elapsed_time = time.time() - init_time
        if elapsed_time > burnout_time:
            end()
        else:
            do_math()


if __name__ == "__main__":
    setup()
    main()