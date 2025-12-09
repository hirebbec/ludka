from aiogram import Router, F
from aiogram.types import Message

from service.ticker import TickerService
from service.user import UserService

ticker_router = Router()


@ticker_router.message(F.text == "📊 Все тикеты")
async def get_all_tickers(
    message: Message, users_service: UserService, tickers_service: TickerService
):
    if message.from_user:
        await users_service.get_or_create(message.from_user.id)
        tickers = await tickers_service.get_all()

        await message.answer("\n".join([ticker.name for ticker in tickers]))
