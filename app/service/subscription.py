from db.repository.subscription import SubscriptionRepository
from service.base import BaseService


class SubscriptionService(BaseService):
    def __init__(self, subscription_repository: SubscriptionRepository):
        self._subscription_repository = subscription_repository
