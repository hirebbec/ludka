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
        if isinstance(event, Message) and not event.from_user:
            return None

        session = data.get("session")

        user_repository = UserRepository(session=session)  # type: ignore
        subscription_repository = SubscriptionRepository(session=session)  # type: ignore

        user_service = UserService(user_repository=user_repository)
        subscription_service = SubscriptionService(
            subscription_repository=subscription_repository
        )
        stock_service = StockService()

        if isinstance(event, Message) and event.from_user:
            if not await user_service.get_or_create(telegram_id=event.from_user.id):
                return None

        data["user_service"] = user_service
        data["subscription_service"] = subscription_service
        data["stock_service"] = stock_service

        return await handler(event, data)
