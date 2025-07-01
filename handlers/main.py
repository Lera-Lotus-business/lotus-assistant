from aiogram import types, Dispatcher

async def handle_news(message: types.Message):
    await message.answer("🗞 Новости туризма: Ещё не подключены. Ожидайте обновление.")

async def handle_idea(message: types.Message):
    await message.answer("💡 Идея: Скоро появится генерация от ИИ!")

async def handle_plan(message: types.Message):
    await message.answer("📅 План на день: Сегодня фокус на задаче №1 — доработка функционала бота.")

async def handle_villar(message: types.Message):
    await message.answer("📊 Проект Villar Marina: Раздел в разработке. Будет доступен позже.")

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(handle_news, lambda msg: msg.text == "🗞 Новости туризма")
    dp.register_message_handler(handle_idea, lambda msg: msg.text == "💡 Получить идею")
    dp.register_message_handler(handle_plan, lambda msg: msg.text == "📅 План на день")
    dp.register_message_handler(handle_villar, lambda msg: msg.text == "📊 Проект Villar Marina")
