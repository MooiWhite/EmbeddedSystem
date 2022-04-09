import time
from gpiozero import MotionSensor, LED

pir = MotionSensor(4)
led=LED(16)

while True:
    if pir.motion_detected:
        print("Motion detected")
        led.on()
        time.sleep(1)
    else:
        print("No motion")
        led.off()
        time.sleep(1)