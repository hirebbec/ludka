from aiogram import BaseMiddleware

from db.repository.user import UserRepository
from service.user import UserService

from db.repository.subscription import SubscriptionRepository
from service.subscription import SubscriptionService

from service.ticker import TickerService


class ServiceMiddleware(BaseMiddleware):
    async def __call__(self, handler, event, data):
        session = data.get("session")

        users_repo = UserRepository(session)
        subs_repo = SubscriptionRepository(session)

        data["users_service"] = UserService(users_repo)
        data["subscriptions_service"] = SubscriptionService(subs_repo)
        data["tickers_service"] = TickerService()

        return await handler(event, data)
