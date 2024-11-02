import telebot,threading,time

bot = telebot.TeleBot("7223928760:AAEnnfc58NBgdnO1YVFT0VTPc2akQtfRYfU")

def alert(message,text):
	while True:
		time.sleep(86400)
		bot.send_message(message.chat.id,text)	

@bot.message_handler(commands=["start"])
def _start(message):
	bot.reply_to(message,"""دز الاوامر هيج

/alert الرسالة

وراح ادزها الك يومية بهيج وقت وتدلل حبيبي
""")

@bot.message_handler(commands=["alert"])
def _alert(message):
	text = message.text.split("/alert ")[1]
	bot.reply_to(message,"تم يومية راح ادز هيج")
	thread = threading.Thread(target=alert,args=(message,text))
	thread.start()

print("The BOT is UP")
bot.infinity_polling()
