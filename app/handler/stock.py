from turtledemo.nim import Stick

from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from service.stock import StockService
from service.user import UserService
from state.stock import TickerState
from utils.format import format_stocks, format_ticker

router = Router()


@router.message(F.text == "Все тикеры")
async def get_all_stocks(
    message: Message,
    user_service: UserService,
    stock_service: StockService,
):
    if not message.from_user:
        return

    await user_service.get_or_create(message.from_user.id)

    stocks = await stock_service.get_all()

    text = format_stocks(tickers=stocks)

    await message.answer(text, parse_mode="HTML")


@router.message(F.text == "Цена по тикеру")
async def ask_ticker(message: Message, user_service: UserService, state: FSMContext):
    if not message.from_user:
        return

    await user_service.get_or_create(message.from_user.id)

    await message.answer("Введите тикер, например: <b>SBER</b>", parse_mode="HTML")
    await state.set_state(TickerState.waiting_for_ticker)


@router.message(TickerState.waiting_for_ticker)
async def get_stock_info(
    message: Message, state: FSMContext, stock_service: StockService
):
    if message.text:
        ticker = message.text.upper()

        stock = await stock_service.get_by_ticker(ticker=ticker)

        if not stock:
            await message.answer("❌ Тикер не найден. Попробуйте снова.")
        else:
            text = format_ticker(ticker=stock)
            await message.answer(text, parse_mode="HTML")

        await state.clear()
