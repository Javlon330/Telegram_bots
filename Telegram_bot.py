Token = '2070214263:AAFsnDYqNDYay3lknPqC_L4Tb9Br2Z275sY'
import telebot
bot = telebot.TeleBot(Token, parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Sherzod nichiksan")

bot.polling()