from schema.base import BaseSchema
from schema.mixins import IDSchema, CreatedAtSchema, UpdatedAtSchema


class CreateSubscriptionSchema(BaseSchema):
    user_id: int
    ticker: str


class UpdateSubscriptionSchema(CreateSubscriptionSchema):
    pass


class GetSubscriptionSchema(
    UpdateSubscriptionSchema, IDSchema, CreatedAtSchema, UpdatedAtSchema
):
    pass


class DeleteSubscriptionSchema(CreateSubscriptionSchema):
    pass
