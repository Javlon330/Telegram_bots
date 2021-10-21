from transliterate import to_cyrillic, to_latin
Token = '2070214263:AAFsnDYqNDYay3lknPqC_L4Tb9Br2Z275sY'
import telebot
bot = telebot.TeleBot(Token, parse_mode=None)
@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Salom.")
@bot.message_handler(func=lambda m: True)
def echo_all(message):
	msg = message.text
	if msg == 'salom':
		javob = 'hayr'
		bot.reply_to(message, javob)
	elif msg == 'hayr':
		javob = "Ko'rishguncha"
		bot.reply_to(message, javob)
bot.polling()