#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.
import os
from gpiozero import LED
import telebot

led= LED(17)
API_TOKEN = '5241059719:AAHiU-DeNzzwJrvOToPuz7V9qRDfDvWj-Lk'

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    chat_id = message.chat.id
    print(chat_id)
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

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)



bot.infinity_polling()
