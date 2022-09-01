import logging
from google.cloud import dialogflow_v2 as df
from telegram import Bot

logger = logging.getLogger(__file__)


class TelegramLogsHandler(logging.Handler):
    def __init__(self, token, chat_id):
        super().__init__()
        self.chat_id = chat_id
        self.tg_bot = Bot(token)

    def emit(self, record):
        log_entry = self.format(record)
        self.tg_bot.send_message(chat_id=self.chat_id, text=log_entry)


def detect_intent_texts(project_id, session_id, text, language_code='ru-RU'):
    """Returns the result of detect intent with texts as inputs.
    Using the same `session_id` between requests allows continuation
    of the conversation."""

    session_client = df.SessionsClient()
    session = session_client.session_path(project_id, session_id)
    text_input = df.TextInput(text=text, language_code=language_code)
    query_input = df.QueryInput(text=text_input)
    response = session_client.detect_intent(
        request={"session": session, "query_input": query_input}
    )

    return response.query_result.intent.is_fallback, response.query_result.fulfillment_text
