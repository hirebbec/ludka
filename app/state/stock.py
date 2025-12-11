from aiogram.fsm.state import StatesGroup, State


class TickerState(StatesGroup):
    waiting_for_ticker = State()
