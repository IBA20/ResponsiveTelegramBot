import os
import logging
import utilities
from telegram import Update
from telegram.ext import Updater, CallbackContext, CommandHandler, MessageHandler, Filters

logger = logging.getLogger(__file__)


def start(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Здравствуйте")


def get_reply_message(update: Update, context: CallbackContext):
    fallback, reply_text = utilities.detect_intent_texts(
        os.environ['GOOGLE_CLOUD_PROJECT'], 
        update.effective_chat.id, 
        update.message.text,
    )
    context.bot.send_message(chat_id=update.effective_chat.id, text=reply_text)


def main():
    logger.setLevel(logging.INFO)
    handler = utilities.TelegramLogsHandler(
        os.environ['TG_BOT_TOKEN'], 
        os.environ['TG_CHATID'],
    )
    handler.setFormatter(
        logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
    )
    logger.addHandler(handler)
    
    updater = Updater(token=os.environ['TG_BOT_TOKEN'])    
    dispatcher = updater.dispatcher
    
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)
    dialog_handler = MessageHandler(
        Filters.text & (~Filters.command), 
        get_reply_message
    )
    dispatcher.add_handler(dialog_handler)
    try:
        logger.info('Support service bot started')
        updater.start_polling()
    except Exception:
        logger.exception('Exception:')


if __name__ == '__main__':
    main()