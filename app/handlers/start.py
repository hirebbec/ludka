from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from sqlalchemy.ext.asyncio import AsyncSession

from keyboards.main import main_keyboard

router = Router()


@router.message(Command("start"))
async def start_cmd(message: Message, session: AsyncSession):
    await message.answer(
        "Привет! Я бот для мониторинга акций 🟢", reply_markup=main_keyboard
    )
