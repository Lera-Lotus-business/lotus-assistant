from aiogram import types, Dispatcher

async def cmd_info(message: types.Message):
    await message.answer("📊 Проект Villar Marina — это event-курорт с яхт-клубом, spa, резиденциями и интеллектуальным клубом. Скоро расскажу подробнее!")

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(cmd_info, lambda msg: msg.text == "📊 Проект Villar Marina")
