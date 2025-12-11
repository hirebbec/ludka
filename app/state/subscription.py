from aiogram.fsm.state import StatesGroup, State


class CreateSubscriptionState(StatesGroup):
    waiting_for_ticker = State()


class DeleteSubscriptionState(StatesGroup):
    waiting_for_ticker = State()
