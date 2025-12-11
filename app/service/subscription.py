from typing import Sequence

from db.repository.subscription import SubscriptionRepository
from schema.subscription import (
    GetSubscriptionSchema,
    CreateSubscriptionSchema,
    DeleteSubscriptionSchema,
)
from service.base import BaseService


class SubscriptionService(BaseService):
    def __init__(self, subscription_repository: SubscriptionRepository):
        self._subscription_repository = subscription_repository

    async def get_by_user_id(self, user_id: int) -> Sequence[GetSubscriptionSchema]:
        return await self._subscription_repository.get_by_user_id(user_id=user_id)

    async def create_subscription(self, ticker: str, user_id: int) -> None:
        await self._subscription_repository.create(
            CreateSubscriptionSchema(ticker=ticker, user_id=user_id)
        )

    async def delete_subscription(self, ticker: str, user_id: int) -> None:
        await self._subscription_repository.delete(
            DeleteSubscriptionSchema(ticker=ticker, user_id=user_id)
        )
