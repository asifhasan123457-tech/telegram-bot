import os
import telebot

TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, "হ্যালো! বট চালু আছে ✅")

@bot.message_handler(commands=["balance"])
def balance(message):
    bot.reply_to(message, "আপনার ব্যালেন্স: $0.00")

@bot.message_handler(commands=["withdraw"])
def withdraw(message):
    bot.reply_to(message, "Withdraw সিস্টেম শীঘ্রই চালু হবে।")

bot.infinity_polling()
