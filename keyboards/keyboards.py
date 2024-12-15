from aiogram import types
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

async def menu_kb():
    menu = InlineKeyboardBuilder()
    menu.row(types.InlineKeyboardButton(text="Хочу получить поздравление от бота", callback_data="greeting"))
    menu.row(types.InlineKeyboardButton(text="Поиграть в монетку", callback_data="money"))
    menu.row(types.InlineKeyboardButton(text="Отправить поздравление другу", callback_data="greeting_to_friend"))
    return menu.as_markup()