import os
import random
import logging
import vk_api as vk
import utilities
from vk_api.longpoll import VkLongPoll, VkEventType

logger = logging.getLogger(__file__)


def get_reply_message(event, vk_api):
    fallback, reply_text = utilities.detect_intent_texts(
        os.environ['GOOGLE_CLOUD_PROJECT'], 
        event.user_id, 
        event.text,
    )
    if not fallback:
        vk_api.messages.send(
            user_id=event.user_id,
            message=reply_text,
            random_id=random.randint(1,1000)
        )


if __name__ == "__main__":
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

    try:
        logger.info('Support service bot started')
        vk_session = vk.VkApi(token=os.environ['VK_TOKEN'])
        vk_api = vk_session.get_api()
        longpoll = VkLongPoll(vk_session)
        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                get_reply_message(event, vk_api)
    except Exception:
        logger.exception('Exception:')
