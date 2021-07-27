import logging
import telegram
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv("TOKEN")

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

bot = telegram.Bot(token=token)
print('------------------------------------------WHO I AM')
print(bot.get_me())

print('---------------------------------------WHO SENDs ME ')
updates = bot.get_updates()
print(updates[0])

name = updates[0]['message']['chat']['username']
bot.send_message(text='Hi ' + name, chat_id=751034701)
