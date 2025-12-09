from db.repository.user import UserRepository
from schemas.user import CreateUserSchema
from service.base import BaseService


class UserService(BaseService):
    def __init__(self, user_repository: UserRepository):
        self._user_repository = user_repository

    async def get_or_create(self, telegram_id: int) -> None:
        user = await self._user_repository.get_by_telegram_id(telegram_id=telegram_id)

        if not user:
            await self._user_repository.create(
                CreateUserSchema(telegram_id=telegram_id)
            )
