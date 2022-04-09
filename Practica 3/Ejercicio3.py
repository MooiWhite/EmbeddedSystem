from bluedot import BlueDot
from gpiozero import PWMLED
from signal import pause

def set_brightnessG(pos):
    brightness = (pos.y + 1) / 2
    green.value = brightness

def set_brightnessA(pos):
    brightness = (pos.y + 1) / 2
    ambar.value = brightness
    
def set_brightnessR(pos):
    brightness = (pos.y + 1) / 2
    red.value = brightness

def dpad(pos):
    if pos.top:
        bd.when_moved = set_brightnessG
        print("Green")
    elif pos.left:
        bd.when_moved = set_brightnessA
        print("Ambar")
    elif pos.right:
        bd.when_moved = set_brightnessR
        print("Red")
    
green = PWMLED(17)
ambar = PWMLED(27)
red   = PWMLED(22)

bd = BlueDot()
bd.when_pressed = dpad

pause()