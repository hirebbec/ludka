from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from service.ticker import TickerService
from service.user import UserService
from state.ticker import TickerState
from utils.format import format_ticker_list, format_ticker

ticker_router = Router()


@ticker_router.message(F.text == "Все тикеры")
async def get_all_tickers(
    message: Message,
    users_service: UserService,
    tickers_service: TickerService,
):
    if not message.from_user:
        return

    await users_service.get_or_create(message.from_user.id)

    tickers = await tickers_service.get_all()

    text = format_ticker_list(tickers=tickers)

    await message.answer(text, parse_mode="HTML")


@ticker_router.message(F.text == "Цена по тикеру")
async def ask_ticker(message: Message, users_service: UserService, state: FSMContext):
    if not message.from_user:
        return

    await users_service.get_or_create(message.from_user.id)

    await message.answer("Введите тикер, например: <b>SBER</b>", parse_mode="HTML")
    await state.set_state(TickerState.waiting_for_ticker)


@ticker_router.message(TickerState.waiting_for_ticker)
async def get_ticker_price(
    message: Message, state: FSMContext, tickers_service: TickerService
):
    if message.text:
        secid = message.text.upper()

        ticker = await tickers_service.get_by_secid(secid)

        if not ticker:
            await message.answer("❌ Тикер не найден. Попробуйте снова.")
        else:
            text = format_ticker(ticker=ticker)
            await message.answer(text, parse_mode="HTML")

        await state.clear()
