import os
from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler, Filters
import logging
from telegram import Update
from src.final_test.painter import ml_paint_image

updater = Updater(token=os.environ['telegram_bot_token'], use_context=True)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


def start(update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="This bot can paint your black-white .jpeg pictures, just try it.")


def unknown(update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Sorry, I didn't understand this command.")


def paint_image(update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Wait a moment, picture is processing...")
    images = update.message.photo
    image = context.bot.get_file(images[-1])
    image.download(f'{update.effective_chat.username}_loaded_image.jpg')
    ml_paint_image(update.effective_chat.username)
    context.bot.send_photo(chat_id=update.effective_chat.id,
                           photo=open(f'{update.effective_chat.username}_painted_image.png', 'rb'))


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

unknown_handler = MessageHandler(Filters.text, unknown)
dispatcher.add_handler(unknown_handler)

painter_handler = MessageHandler(Filters.photo, paint_image)
dispatcher.add_handler(painter_handler)

updater.start_polling()
