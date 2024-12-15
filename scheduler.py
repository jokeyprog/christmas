from bot.create_bot import schedul, bot
import datetime
from database import db


async def send_message(id_tg):
    text = await db.get_greeting()
    await bot.send_message(chat_id=id_tg, text=text['text'])


async def schedule():
    users = await db.get_users()
    for user in users:
        if user['send_greetings'] != 0:
            await add_scheduler(id_user=user['id_tg'])


async def add_scheduler(id_user):
    schedul.add_job(send_message, 'date', run_date=datetime.datetime(int(datetime.datetime.today().year)+1,1, 1, 00, 00,00), args=[id_user])


async def remove_jobs_from_scheduler():
    schedul.remove_all_jobs('default')
