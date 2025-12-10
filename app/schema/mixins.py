from datetime import datetime

from schema.base import BaseSchema


class IDSchema(BaseSchema):
    id: int


class CreatedAtSchema(BaseSchema):
    created_at: datetime


class UpdatedAtSchema(BaseSchema):
    updated_at: datetime | None = None
