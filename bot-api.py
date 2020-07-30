import telebot
import io
from OCR import *


bot = telebot.TeleBot('962674884:AAGPIuJ6JNAC-35wGp7fQnLr_2wUKTet0xk')


@bot.message_handler(commands=['start', 'help'])
def start_welcome(message):
    bot.reply_to(message, "Hi!\nPlease send me image ;)")


@bot.message_handler(content_types=['photo', 'image', 'document'])
def handle_doc_image(message):
    try:
        chat_id = message.chat.id
        file_info = bot.get_file(message.photo[-1].file_id)
        download_file = bot.download_file(file_info.file_path)
        image = io.BytesIO(download_file)
        text = preprocess_image(image)

        bot.reply_to(message, text)
        '''
        print(download_file)

        src = "C:/Users/malin/Desktop/Python/OCRBOT/photo" + file_info.file_path.split('/')[-1]
        with open(src, "wb") as new_file:
            new_file.write(download_file)

        bot.reply_to(message, "Received image")'''
    except Exception as e:
        bot.reply_to(message, e)


bot.polling(none_stop=True)





