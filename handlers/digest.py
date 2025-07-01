from aiogram import types, Dispatcher

async def cmd_digest(message: types.Message):
    await message.answer("📰 Пока что я только учусь собирать дайджесты.\nСкоро здесь будет свежая сводка по туризму и отельному бизнесу!")

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(cmd_digest, commands=["digest"])
    dp.register_message_handler(cmd_digest, lambda msg: msg.text == "📰 Новости туризма")
