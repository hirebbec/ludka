from sqlalchemy import select, insert

from db.models import User
from db.repository.base import BaseDataBaseRepository
from schema.user import GetUserSchema, CreateUserSchema


class UserRepository(BaseDataBaseRepository):
    async def get_by_telegram_id(self, telegram_id: int) -> GetUserSchema | None:
        query = select(User).where(User.telegram_id == telegram_id)

        result = await self._session.execute(query)
        return (
            GetUserSchema.model_validate(result.scalars().first()) if result else None
        )

    async def create(self, user: CreateUserSchema) -> GetUserSchema | None:
        query = insert(User).values(**user.model_dump()).returning(User)

        result = await self._session.execute(query)
        row_user = result.fetchone()

        return GetUserSchema.model_validate(row_user[0]) if row_user else None
