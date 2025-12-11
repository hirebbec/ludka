from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from service.subscription import SubscriptionService
from service.user import UserService
from state.subscription import CreateSubscriptionState, DeleteSubscriptionState
from utils.format import format_subscriptions

router = Router()


@router.message(F.text == "Мои подписки")
async def get_subscriptions_by_user_id(
    message: Message,
    user_service: UserService,
    subscription_service: SubscriptionService,
):
    if not message.from_user:
        return

    user = await user_service.get_or_create(message.from_user.id)

    subscriptions = await subscription_service.get_by_user_id(user_id=user.telegram_id)

    text = format_subscriptions(subscriptions=subscriptions)

    await message.answer(text, parse_mode="HTML")


@router.message(F.text == "Добавить подписку")
async def ask_ticker_for_create_subscription(
    message: Message, user_service: UserService, state: FSMContext
):
    if not message.from_user:
        return

    await user_service.get_or_create(message.from_user.id)

    await message.answer("Введите тикер, например: <b>SBER</b>", parse_mode="HTML")
    await state.set_state(CreateSubscriptionState.waiting_for_ticker)


@router.message(F.text == "Удалить подписку")
async def ask_ticker_for_create_subscription(
    message: Message, user_service: UserService, state: FSMContext
):
    if not message.from_user:
        return

    await user_service.get_or_create(message.from_user.id)

    await message.answer("Введите тикер, например: <b>SBER</b>", parse_mode="HTML")
    await state.set_state(DeleteSubscriptionState.waiting_for_ticker)


@router.message(CreateSubscriptionState.waiting_for_ticker)
async def create_subscription(
    message: Message, subscription_service: SubscriptionService
):
    if message.text:
        ticker = message.text.upper()

        await subscription_service.create_subscription(
            ticker=ticker, user_id=message.from_user.id
        )
        await message.answer("Подписка добавлена!", parse_mode="HTML")


@router.message(DeleteSubscriptionState.waiting_for_ticker)
async def delete_subscription(
    message: Message, subscription_service: SubscriptionService
):
    if message.text:
        ticker = message.text.upper()

        await subscription_service.delete_subscription(
            ticker=ticker, user_id=message.from_user.id
        )
        await message.answer("Подписка удаленна!", parse_mode="HTML")
