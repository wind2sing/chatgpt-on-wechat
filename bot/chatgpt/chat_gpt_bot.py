from bot.bot import Bot
from revChatGPT.Official import Chatbot
from common.log import logger
from config import conf



class ChatGPTBot(Bot):
    def __init__(self):
        self.chatbot = Chatbot(api_key=conf().get('open_ai_api_key'))

    def reply(self, query, context=None):
        logger.info("[OPEN_AI] query={}".format(query))
        try:
            response = self.chatbot.ask(query)
            res_content = response.choices[0]["text"].strip() 
        except Exception as e:
            logger.exception(e)
            return None
        logger.info("[OPEN_AI] reply={}".format(res_content))
        return res_content
