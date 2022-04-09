from bluedot import BlueDot
from signal import pause
import RPi.GPIO as GPIO
#https://pypi.org/project/raspberrypi-tm1637/
#pip3 install raspberrypi-tm1637
import tm1637 

display = tm1637.TM1637(clk=2, dio=3)


def Juan():
  display.show('juan')
def Christian():
  display.show('chri')
def MarianaDiego(pos):
  if(pos.y > 0):
    display.show('mari')
  else:
    display.show('dieg')
bd = BlueDot()
bd.when_pressed = Juan
bd.when_released = Christian
bd.when_moved = MarianaDiego
pause()
