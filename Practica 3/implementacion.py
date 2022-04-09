import os
from bluedot import BlueDot
from gpiozero import LED
from signal import pause
import telebot

bd = BlueDot()
led = LED(27)
API_TOKEN = '5241059719:AAHiU-DeNzzwJrvOToPuz7V9qRDfDvWj-Lk'
bot = telebot.TeleBot(API_TOKEN)
chat_id = '1068817370'

def dpad(pos):
  if pos.top:
    led.on()
  elif pos.bottom:
    led.off()
  elif pos.left:
    bot.send_message(chat_id,"""\
    La temperatura actual es de: 25\
    """)
  elif pos.right:
    bot.send_message(chat_id,"""\
    Alimentando a la mascota\
    """)
  elif pos.middle:
    bot.send_message(chat_id,"""\
    Realizando fotografia\
    """)

bd.when_pressed = dpad
pause()
