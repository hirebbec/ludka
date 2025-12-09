import asyncio
from bot import bot, dp
from handlers import routers


async def main():
    for rt in routers:
        dp.include_router(rt)

    print("Bot start")
    await dp.start_polling(bot, polling_timeout=10)


if __name__ == "__main__":
    asyncio.run(main())
