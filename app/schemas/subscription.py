from schemas.base import BaseSchema


class CreateSubscriptionSchema(BaseSchema):
    user_id: int
    ticker: str


class UpdateSubscriptionSchema(CreateSubscriptionSchema):
    pass


class GetSubscriptionSchema(UpdateSubscriptionSchema):
    pass
