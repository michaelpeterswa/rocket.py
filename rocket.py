# michaelpeterswa
# rocket.py
# 02.21.21

# import Raspberry Pi GPIO module
import RPi.GPIO as GPIO
import time
import csv

def setup():

    # Initialize pinout
    GPIO.setmode(GPIO.board)

    # Set pins
    accel = None # accelerometer pin
    servo = None # servo pin

    GPIO.setup(accel, GPIO.IN)
    GPIO.setup(servo, GPIO.OUT)

def do_math():
    print("doing math")
    data = 0
    # data2 = 1

    return data
    # return data, data2

# out_data, out_data2 = do_math()

def end():
    print("cleaning up")

def main():
    init_time = time.time()
    burnout_time = 10 # time in seconds
    launched = False

    acceleration = 0
    acceleration = 10

    if acceleration > 1 and not launched:
        launched = True

    flight_data = []
    while launched:
        elapsed_time = time.time() - init_time
        
        if elapsed_time > burnout_time:
            launched = False
            end()
        else:
            data = do_math()
        
        flight_data.append((elapsed_time, data))

    with open("data.csv", 'w') as f:
        csvwriter = csv.writer(f)
        for row in flight_data:
            csvwriter.writerow(row)


if __name__ == "__main__":
    setup()
    main()