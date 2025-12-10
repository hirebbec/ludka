from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Все тикеры"),
            KeyboardButton(text="Цена по тикеру"),
        ],
        [
            KeyboardButton(text="Мои подписки"),
            KeyboardButton(text="Цена по моим подпискам"),
        ],
        [
            KeyboardButton(text="Добавить подписку"),
            KeyboardButton(text="Удалить подписку"),
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=False,
)
