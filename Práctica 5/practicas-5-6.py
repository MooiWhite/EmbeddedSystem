import telebot
from gpiozero import Servo
from time import sleep
from gpiozero.pins.pigpio import PiGPIOFactory

factory = PiGPIOFactory()
 
myGPIO=12
servo = Servo(myGPIO,min_pulse_width=0.5/1000,max_pulse_width=2.5/1000, pin_factory=factory)

API_TOKEN = '5241059719:AAHiU-DeNzzwJrvOToPuz7V9qRDfDvWj-Lk'
bot = telebot.TeleBot(API_TOKEN)

#servo.mid()
#servo.value = 0;
@bot.message_handler(commands=['pet'])
def turn_on(message):
    bot.reply_to(message,"""\
    alimentando a la mascota\
    """)
    for i in range(3):
        servo.value = 0.45;
        sleep(5)
        servo.value = 0.0;
        sleep(5)


bot.infinity_polling()