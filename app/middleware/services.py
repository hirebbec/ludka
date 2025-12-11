from typing import Any, Dict, Callable, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import Message, TelegramObject

from db.repository.user import UserRepository
from service.user import UserService

from db.repository.subscription import SubscriptionRepository
from service.subscription import SubscriptionService

from service.stock import StockService


class ServiceMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:
        session = data.get("session")

        users_repo = UserRepository(session)
        subs_repo = SubscriptionRepository(session)

        user_service = UserService(users_repo)
        subscription_service = SubscriptionService(subs_repo)
        stock_service = StockService()

        if isinstance(event, Message) and event.from_user:
            await user_service.get_or_create(event.from_user.id)

        data["user_service"] = user_service
        data["subscription_service"] = subscription_service
        data["stock_service"] = stock_service

        return await handler(event, data)
