from typing import Sequence

from sqlalchemy import insert, select, delete

from db.models import Subscription
from db.repository.base import BaseDataBaseRepository
from schema.subscription import (
    CreateSubscriptionSchema,
    GetSubscriptionSchema,
    DeleteSubscriptionSchema,
)


class SubscriptionRepository(BaseDataBaseRepository):
    async def create(self, subscription: CreateSubscriptionSchema) -> None:
        query = insert(Subscription).values(**subscription.model_dump())

        await self._session.execute(query)
        await self._session.flush()

    async def get_by_user_id(self, user_id: int) -> Sequence[GetSubscriptionSchema]:
        query = select(Subscription).where(Subscription.user_id == user_id)

        result = await self._session.execute(query)
        return [
            GetSubscriptionSchema.model_validate(subscription)
            for subscription in result.scalars().all()
        ]

    async def delete(self, subscription: DeleteSubscriptionSchema) -> None:
        query = delete(Subscription).where(
            Subscription.user_id == subscription.user_id,
            Subscription.ticker == subscription.ticker,
        )

        await self._session.execute(query)
        await self._session.flush()
