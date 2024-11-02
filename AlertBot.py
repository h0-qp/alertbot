import threading,time,asyncio
from telebot.async_telebot import AsyncTeleBot
from keepAlive import keep_alive
bot = AsyncTeleBot("7223928760:AAEnnfc58NBgdnO1YVFT0VTPc2akQtfRYfU")	

@bot.message_handler(commands=["start"])
async def _start(message):
	await bot.reply_to(message,"""دز الاوامر هيج

/alert الرسالة

وراح ادزها الك يومية بهيج وقت وتدلل حبيبي
""")

@bot.message_handler(commands=["alert"])
async def _alert(message):
	text = message.text.split("/alert ")[1]
	await bot.reply_to(message,"تم يومية راح ادز هيج")
	while True:
		await asyncio.sleep(86400)
		await bot.send_message(message.chat.id,text)

print("The BOT is UP")
keep_alive()
asyncio.run(bot.infinity_polling())
