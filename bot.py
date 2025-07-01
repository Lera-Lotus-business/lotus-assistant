from aiogram import Bot, Dispatcher, executor, types
from handlers import start, main  # <-- добавили main
from config import BOT_TOKEN
import logging

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# Регистрируем обработчики команд
start.register_handlers(dp)
main.register_handlers(dp)  # <-- добавили регистрацию нового файла

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
