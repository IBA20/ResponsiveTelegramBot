import os
import logging
import neurnet as nn
from telegram import Update
from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler, Filters



def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Здравствуйте")

# def echo(update: Update, context: CallbackContext):
#     context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

def dialog(update: Update, context: CallbackContext):
    fallback, reply_text = nn.detect_intent_texts(os.environ['GOOGLE_CLOUD_PROJECT'], update.effective_chat.id, update.message.text)
    context.bot.send_message(chat_id=update.effective_chat.id, text=reply_text)

def main():
    logger = logging.getLogger(__file__)
    logger.setLevel(logging.INFO)
    handler = nn.TelegramLogsHandler()
    handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    logger.addHandler(handler)
    
    updater = Updater(token=os.environ['TG_BOT_TOKEN'])    
    dispatcher = updater.dispatcher
    
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)
    # echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
    # dispatcher.add_handler(echo_handler)
    dialog_handler = MessageHandler(Filters.text & (~Filters.command), dialog)
    dispatcher.add_handler(dialog_handler)
    try:
        logger.info('Support service bot started')
        updater.start_polling()
    except Exception:
        logger.exception('Exception:')


if __name__ == '__main__':
    main()