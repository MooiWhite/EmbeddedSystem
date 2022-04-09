#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.
import os
from gpiozero import LED
import telebot

#Importacion de sensor de temperatura
import time                             #Importamos el paquete time
from w1thermsensor import W1ThermSensor #Importamos el paquete W1ThermSensor

led = LED(17)
sensor = W1ThermSensor() #Creamos el objeto sensor
API_TOKEN = '5241059719:AAHiU-DeNzzwJrvOToPuz7V9qRDfDvWj-Lk'

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hola Ingenieros, soy Charly, su primer bot!.
Escriban un mensaje para realizar un echo.\
""")
    
    
@bot.message_handler(commands=['apaga'])
def turn_off(message):
    led.off()
    bot.reply_to(message,"""\
    se apago\
    """)

@bot.message_handler(commands=['enciende'])
def turn_on(message):
    led.on()
    bot.reply_to(message,"""\
    se encendio\
    """)

@bot.message_handler(commands=['temp'])
def get_temp_sens(message):
    alarma = 0
    while True:
        tfile = open("/sys/bus/w1/devices/28-012062308a5e/w1_slave")
        text = tfile.read()
        tfile.close()
        secondline = text.split("\n")[1]
        temperaturedata = secondline.split(" ")[9]
        temperature = float(temperaturedata[2:])
        temperature = int(temperature / 1000)
        if temperature > 30:
            led.on()
            if alarma == 0:
                alarma = 1
                bot.reply_to(message,"""\
                temperatura alta\
                """)
        else:
            alarma = 0
            led.off()

bot.infinity_polling()
