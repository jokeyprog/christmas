import datetime

from bot.create_bot import schedul, bot
from database import db


async def send_message_for_users(id_tg):
    text = await db.get_greeting()
    await bot.send_message(chat_id=id_tg, text=text['text'])

async def send_message_for_friend(id_tg_recipient, text):
    await bot.send_message(chat_id=id_tg_recipient, text=text)


async def schedule():
    users = await db.get_users()
    for user in users:
        if user['send_greetings'] != 0:
            await add_scheduler_for_users(id_user=user['id_tg'])
    friends = await db.get_all_for_friends()
    for friend in friends:
        await add_scheduler_for_friends(friend['id_tg_recipient'], friend['greeting'])


async def add_scheduler_for_users(id_user):
    schedul.add_job(send_message_for_users, 'date', run_date=datetime.datetime(int(datetime.datetime.today().year)+1,1, 1, 00, 00,00), args=[id_user])


async def add_scheduler_for_friends(id_tg_recipient, text):
    schedul.add_job(send_message_for_friend, 'date', run_date=datetime.datetime(int(datetime.datetime.today().year)+1, 1, 1, 00, 00, 00), args=[id_tg_recipient, text])


async def remove_jobs_from_scheduler():
    schedul.remove_all_jobs('default')
