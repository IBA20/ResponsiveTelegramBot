import os
import logging
from telegram import Update
from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler, Filters
from neurnet import detect_intent_texts


def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Здравствуйте")

# def echo(update: Update, context: CallbackContext):
#     context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

def dialog(update: Update, context: CallbackContext):
    fallback, reply_text = detect_intent_texts(os.environ['GOOGLE_CLOUD_PROJECT'], update.effective_chat.id, update.message.text)
    context.bot.send_message(chat_id=update.effective_chat.id, text=reply_text)

def main():
    updater = Updater(token=os.environ['TG_BOT_TOKEN'])    
    dispatcher = updater.dispatcher
    
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)
    # echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
    # dispatcher.add_handler(echo_handler)
    dialog_handler = MessageHandler(Filters.text & (~Filters.command), dialog)
    dispatcher.add_handler(dialog_handler)
    
    updater.start_polling()

if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                         level=logging.INFO)
    main()