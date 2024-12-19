from aiogram import types
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

async def menu_kb():
    menu = InlineKeyboardBuilder()
    menu.row(types.InlineKeyboardButton(text="Хочу получить поздравление от бота", callback_data="greeting"))
    menu.row(types.InlineKeyboardButton(text="Поиграть в монетку", callback_data="money"))
    menu.row(types.InlineKeyboardButton(text="Отправить поздравление другу", callback_data="greeting_to_friend"))
    menu.row(types.InlineKeyboardButton(text="Посмотреть отправленные поздравления", callback_data="get_friends"))
    return menu.as_markup()


async def change_kb():
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(text="Удалить поздравление", callback_data="delete"))
    return builder.as_markup()

async def cancel_kb():
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(text="Отменить ввод", callback_data="cancel"))
    return builder.as_markup()
