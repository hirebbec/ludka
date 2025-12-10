from aiogram import Bot, Dispatcher

from config import settings
from middleware.db import DbSessionMiddleware
from middleware.logger import LoggingMiddleware
from middleware.services import ServiceMiddleware

bot = Bot(token=settings().TOKEN)

dp = Dispatcher()

dp.update.middleware(LoggingMiddleware())
dp.callback_query.middleware(LoggingMiddleware())

dp.update.middleware(DbSessionMiddleware())
dp.update.middleware(ServiceMiddleware())
