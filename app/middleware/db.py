from aiogram import BaseMiddleware
from db.session import get_session


class DbSessionMiddleware(BaseMiddleware):
    async def __call__(self, handler, event, data):
        async with get_session() as session:
            data["session"] = session
            return await handler(event, data)
