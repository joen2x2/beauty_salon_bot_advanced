import telebot

TOKEN = "..."  #cекретный ключ к боту
bot = telebot.TeleBot(TOKEN) #инициализация бота


@bot.message_handler(commands=["start"])#обработка команд
def handle_start(message):
    bot.send_message(message.chat.id, "Привет, я бот")

@bot.message_handler(func=lambda message: True)#обработка сообщений в чат;этот код должен быть внизу
def handle_all(message):
        bot.send_message(message.chat.id, "Не понял! Набери /start")

if __name__ == "__main__": #бот будет постоянно прослушивать чаты
    bot.polling(none_stop=True) #чтобы бот в случае ошибки продолжил работать
