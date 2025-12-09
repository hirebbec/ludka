from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()


@router.message(Command("stock"))
async def stock_cmd(message: Message):
    await message.answer("Пока что я не знаю акций 😔 Но скоро научусь!")
