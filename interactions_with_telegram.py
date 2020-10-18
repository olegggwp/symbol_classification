import telebot

VERSION_OF_BOT = "0.1"
AUTHOR = "olegggwp"

bot = telebot.TeleBot('1055555890:AAGr04hFiTAM5dRjzzaGOkWqjR_C6MkCz3M')

@bot.message_handler(commands=['start']) # Выполняется, когда пользователь нажимает на start
def send_welcome(message):
    bot.send_message(message.chat.id, "Hello, man")
    bot.send_message(message.chat.id, "There's a bot by " + AUTHOR + " v." + VERSION_OF_BOT)

@bot.message_handler(content_types=["text"]) # Любой текст
def repeat_all_text_messages(message): 
    bot.send_message(message.chat.id, "I see you send me a text message")

@bot.message_handler(content_types=["photo"]) # Любое изображение
def repeat_all_image_messages(message): 
    bot.send_message(message.chat.id, "I see you send me an photo, cool")  

if __name__ == '__main__':
    bot.polling(none_stop=True)