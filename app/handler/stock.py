from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from service.stock import StockService
from service.subscription import SubscriptionService
from state.stock import TickerState
from utils.format import format_stocks, format_ticker

router = Router()


@router.message(F.text == "Все тикеры")
async def get_all(
    message: Message,
    stock_service: StockService,
):
    stocks = await stock_service.get_all()

    text = format_stocks(tickers=stocks)

    await message.answer(text, parse_mode="HTML")


@router.message(F.text == "Цена по тикеру")
async def ask_ticker(message: Message, state: FSMContext):
    await message.answer("Введите тикер, например: <b>SBER</b>", parse_mode="HTML")
    await state.set_state(TickerState.waiting_for_ticker)


@router.message(TickerState.waiting_for_ticker)
async def get_by_ticker(
    message: Message,
    state: FSMContext,
    stock_service: StockService,
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


@router.message(F.text == "Цена по моим подпискам")
async def get_by_subscriptions(
    message: Message,
    subscription_service: SubscriptionService,
    stock_service: StockService,
):
    subscriptions = await subscription_service.get_by_user_id(
        user_id=message.from_user.id
    )

    stocks = [
        await stock_service.get_by_ticker(ticker=subscription.ticker)
        for subscription in subscriptions
    ]
    text = format_stocks(tickers=stocks)

    await message.answer(text, parse_mode="HTML")
