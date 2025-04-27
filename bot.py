import asyncio
from os import getenv

from aiogram import Bot, Dispatcher

from database import create_db
from handlers import router


TOKEN = getenv('BOT_TOKEN')


async def main() -> None:
    await create_db()

    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_router(router)

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
