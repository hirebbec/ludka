from aiogram.fsm.state import StatesGroup, State


class SubscriptionState(StatesGroup):
    waiting_for_ticker = State()
