from aiogram import types, F, Router
from aiogram.filters import Command, StateFilter
from aiogram.filters.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
import random

from keyboards import keyboards as kb
from database import db
import scheduler


router = Router()


class Greetings(StatesGroup):
    username = State()
    text = State()


class DeleteGreetings(StatesGroup):
    username = State()


@router.message(Command("start"))
async def hello_message(message: types.Message):
    if message.from_user.username:
        await db.registration(message.from_user.id, '@' + message.from_user.username)
    else:
        await db.registration(message.from_user.id, None)
    await scheduler.remove_jobs_from_scheduler()
    await scheduler.schedule()
    await message.answer("Привет! Я бот для поднятия новогоднего настроения!",  reply_markup= await kb.menu_kb())


@router.callback_query(F.data == "greeting")
async def reg_on_greeting(callback: types.CallbackQuery):
    await db.send_greetings(callback.from_user.id)
    await callback.answer("Ура! Вы получите поздравление!")
    await callback.message.answer("1 января в 00:00 бот отправит Вам поздравление!")
    await callback.message.answer("Меню", reply_markup= await kb.menu_kb())


@router.callback_query(F.data == "money")
async def money(callback: types.CallbackQuery):
    await callback.answer("Монетка подкинута!")
    await callback.message.answer(f"Ура! Вам выпал {random.choice(['орёл', 'решка'])}!")
    await callback.message.answer("Меню", reply_markup= await kb.menu_kb())


@router.callback_query(F.data == "greeting_to_friend")
async def set_greetings_for_friend(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer("Ваш друг будет счастлив!")
    await callback.message.answer("Отправьте мне username Вашего друга!\nПроследите, чтобы он хотя бы раз запустил "
                                  "этого бота!", reply_markup= await kb.cancel_kb())
    await state.set_state(Greetings.username)


@router.message(StateFilter(Greetings.username))
async def set_name(message: types.Message, state: FSMContext):
    if str(message.text)[0] == "@" and " " not in str(message.text):
        await state.update_data(username=str(message.text))
        await message.answer("А теперь отправьте текст поздравления!", reply_markup= await kb.cancel_kb())
        await state.set_state(Greetings.text)
    elif str(message.text)[0] != "@":
        await message.answer("Все username должны начинаться с @", reply_markup= await kb.cancel_kb())
    elif " " not in str(message.text):
        await message.answer("Username не могут содержать пробелы", reply_markup= await kb.cancel_kb())


@router.message(StateFilter(Greetings.text))
async def set_name(message: types.Message, state: FSMContext):
    await state.update_data(text=str(message.text))
    data = await state.get_data()
    result = await db.set_greetings_for_friend(message.from_user.id, data)
    if result and result != "Вы уже отправили поздравление этому другу":
        await message.answer("1 января в 00:00 Ваш друг получит это сообщение!")
        await scheduler.remove_jobs_from_scheduler()
        await scheduler.schedule()
    elif result == "Вы уже отправили поздравление этому другу":
        await message.answer(result)
    else:
        await message.answer(f"Пользователя с таким username нет в базе данных.\nПопросите своего друга изменить "
                             f"username в боте с помощью /start и попробуйте ещё раз с новым username")
    await message.answer("Меню", reply_markup=await kb.menu_kb())
    await state.clear()


@router.callback_query(F.data == "get_friends")
async def get_friends(callback: types.CallbackQuery):
    await callback.answer("Вот Ваши друзья!")
    result = await db.get_friends(callback.from_user.id)
    message = ''
    if result:
        for res in result:
            message += res
        await callback.message.answer(message, reply_markup=await kb.change_kb())
    else:
        message += "Вы ещё никому не отправили поздравлений"
        await callback.message.answer(message)
    await callback.message.answer("Меню", reply_markup=await kb.menu_kb())


@router.callback_query(F.data == "delete")
async def delete_greeting(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer("Печально, что Вы хотите удалить поздравление для Вашего друга")
    await callback.message.answer("Отправьте username друга, чьё поздравление хотите удалить", reply_markup= await kb.cancel_kb())
    await state.set_state(DeleteGreetings.username)


@router.message(StateFilter(DeleteGreetings.username))
async def get_username_for_delete(message: types.Message, state: FSMContext):
    if str(message.text)[0] == "@" and " " not in str(message.text):
        await state.update_data(username=str(message.text))
        result = await db.delete(message.from_user.id, message.text)
        if result:
            await state.clear()
            await scheduler.remove_jobs_from_scheduler()
            await scheduler.schedule()
            await message.answer("Поздравление успешно удалено!")
        else:
            await message.answer("В Вашем списке поздравлений нет такого пользователя", reply_markup= await kb.cancel_kb())
        await message.answer("Меню", reply_markup=await kb.menu_kb())
    elif str(message.text)[0] != "@":
        await message.answer("Все username должны начинаться с @", reply_markup= await kb.cancel_kb())
    elif " " not in str(message.text):
        await message.answer("Username не могут содержать пробелы", reply_markup= await kb.cancel_kb())


@router.callback_query(F.data == "cancel")
async def cancel(callback: types.CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.answer("Отменено!")
    await callback.message.answer("Меню", reply_markup= await kb.menu_kb())
