import telebot

bot = telebot.TeleBot("6008005129:AAF-rphgvQKcwr1E3oPd1KD93-J8ZBejAhI")

TOKEN = '1609086008005129:AAF-rphgvQKcwr1E3oPd1KD93-J8ZBejAhI'

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу помочь ?")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши Привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю, напиши /help")

#bot.polling(none_stop=True, interval=0)