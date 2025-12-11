from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from keyboard.main import main_keyboard
from service.user import UserService

router = Router()


@router.message(Command("start"))
async def start_cmd(message: Message, user_service: UserService):
    await message.answer(
        "Привет! Я бот для мониторинга акций", reply_markup=main_keyboard
    )
