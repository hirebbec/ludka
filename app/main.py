import asyncio
from bot import bot, dp
from handlers import routers
from middleware.db import DbSessionMiddleware
from middleware.services import ServiceMiddleware


async def main():
    dp.message.middleware(DbSessionMiddleware())
    dp.message.middleware(ServiceMiddleware())

    for rt in routers:
        dp.include_router(rt)

    print("Start")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
