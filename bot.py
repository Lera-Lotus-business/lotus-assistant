from aiogram import Bot, Dispatcher, executor, types
import logging
from config import BOT_TOKEN

from handlers import start, digest, info

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

start.register_handlers(dp)
digest.register_handlers(dp)
info.register_handlers(dp)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
