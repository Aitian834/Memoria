import telebot  
import os  

TOKEN = os.getenv("BOT_TOKEN")  
bot = telebot.TeleBot(TOKEN)  

@bot.message_handler(commands=['start', 'help'])  
def send_welcome(message):  
    bot.reply_to(message, "¡Hola! Soy tu asistente. ¿En qué puedo ayudarte?")  

@bot.message_handler(func=lambda message: True)  
def echo_all(message):  
    bot.reply_to(message, "Dijiste: " + message.text)  

print("Bot en ejecución...")  
bot.polling()  
