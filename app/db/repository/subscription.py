from sqlalchemy import insert, select

from db.models import Subscription
from db.repository.base import BaseDataBaseRepository
from schemas.subscription import CreateSubscriptionSchema, GetSubscriptionSchema


class SubscriptionRepository(BaseDataBaseRepository):
    async def create(self, subscription: CreateSubscriptionSchema) -> None:
        query = insert(Subscription).values(**subscription.model_dump())

        await self._session.execute(query)
        await self._session.flush()

    async def get_by_user_id(self, user_id: int) -> GetSubscriptionSchema | None:
        query = select(Subscription).where(Subscription.user_id == user_id)

        result = await self._session.execute(query)
        return GetSubscriptionSchema.model_validate(result.scalars().first()) if result else None
