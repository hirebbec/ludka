from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()


@router.message(Command("start"))
async def start_cmd(message: Message):
    await message.answer("Привет! Я бот для мониторинга акций 🟢")
