import asyncio

from bot.create_bot import bot, dp, schedul
from bot.handlers import router
from scheduler import schedule


async def main():
    dp.include_router(router)
    schedul.start()
    await bot.delete_webhook(drop_pending_updates=True)
    dp.startup.register(schedule)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
