from aiogram import types, F, Router
# from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from aiogram.filters import Command, StateFilter
from keyboards import keyboards as kb
from database import db
from aiogram.filters.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
# from bot.create_bot import bot

router = Router()


class Greetings(StatesGroup):
    username = State()
    text = State()

@router.message(Command("start"))
async def hello_message(message: types.Message):
    await db.registration(message.from_user.id)
    await message.answer("Привет! Я бот для поднятия новогоднего настроения!",  reply_markup= await kb.menu_kb())


@router.callback_query(F.data == "greeting")
async def reg_on_greeting(callback: types.CallbackQuery, state: FSMContext):
    await db.send_greetings(callback.from_user.id)
    await callback.answer("Вы зарегистрировались!")
    await callback.message.answer("Ура! 1 января в 00:00 бот отправит Вам поздравление!")
    await callback.message.answer("Меню", reply_markup= await kb.menu_kb())


@router.callback_query(F.data == "greeting_to_friend")
async def set_greetings_for_friend(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer("Ваш друг будет счастлив!")
    await callback.message.answer("Отправьте мне юзернейм Вашего друга!\nПроследите, чтобы он хотя бы раз запустил "
                                  "этого бота!")
    await state.set_state(Greetings.username)


@router.message(StateFilter(Greetings.username))
async def set_name(message: types.Message, state: FSMContext):
    await state.update_data(username=str(message.text))
    await message.answer("А теперь отправьте текст поздравления!")
    await state.set_state(Greetings.text)


@router.message(StateFilter(Greetings.text))
async def set_name(message: types.Message, state: FSMContext):
    await state.update_data(text=str(message.text))
    data = await state.get_data()
    await db.set_greetings_for_friend(message.from_user.id, data)
    await message.answer("1 января в 00:00 Ваш друг получит это сообщение, но проследите, чтобы он хотя бы раз запустил"
                         " этого бота!")
    await message.answer("Меню", reply_markup= await kb.menu_kb())
    await state.clear()