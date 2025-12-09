from schemas.base import BaseSchema
from schemas.mixins import CreatedAtSchema, UpdatedAtSchema


class CreateUserSchema(BaseSchema):
    telegram_id: int


class UpdateUserSchema(CreateUserSchema):
    pass


class GetUserSchema(UpdateUserSchema, CreatedAtSchema, UpdatedAtSchema):
    pass
