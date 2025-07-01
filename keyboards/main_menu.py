from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(resize_keyboard=True)
main_menu.add(
    KeyboardButton("📰 Новости туризма"),
    KeyboardButton("📊 Проект Villar Marina"),
)
main_menu.add(
    KeyboardButton("💡 Получить идею"),
    KeyboardButton("🗓 План на день")
)
