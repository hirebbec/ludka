import asyncio
from bot import bot, dp
from handler import routers


async def main():
    for rt in routers:
        dp.include_router(rt)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
