from transliterate import to_cyrillic, to_latin
Token = '2070214263:AAFsnDYqNDYay3lknPqC_L4Tb9Br2Z275sY'
import telebot
bot = telebot.TeleBot(Token, parse_mode=None)
sozlar = ['salom','hayr']
@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Assalom aleykum.Botimizga Hush kelibsiz!!!")
@bot.message_handler(func=lambda m: True)
def echo_all(message):
	msg = message.text
	if msg.isascii():
		javob = to_cyrillic(msg)
	else:
		javob = to_latin(msg)
	bot.reply_to(message, javob )
bot.polling()