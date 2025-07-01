from aiogram import types, Dispatcher
from keyboards.main_menu import main_menu

async def cmd_start(message: types.Message):
    await message.answer("Привет! Я Lotus Assistant. Чем могу быть полезен?", reply_markup=main_menu)

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands=["start"])
