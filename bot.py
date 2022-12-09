from telebot import TeleBot
from telebot.types import Message
from wiki import search_result
from settings import TELEGRAM_TOKEN

bot = TeleBot(TELEGRAM_TOKEN, parse_mode='html')

@bot.message_handler(commands=['start'])
def start(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, f"Salom <b>{message.from_user.first_name}</b>")


@bot.message_handler(content_types=['video', 'photo', 'audio', 'sticker', 'animation'])
def echo(message: Message):
    chat_id = message.chat.id
    bot.copy_message(chat_id, chat_id, message.message_id)


@bot.message_handler(content_types=['text'])
def wiki(message: Message):
    chat_id = message.chat.id
    search_text = message.text
    result = search_result(search_text)
    bot.send_message(chat_id, result)

bot.polling(none_stop=True)
