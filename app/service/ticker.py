from schemas.ticker import GetTickerSchema
from service.base import BaseService


class TickerService(BaseService):
    async def get_all(self) -> list[GetTickerSchema]:
        return [GetTickerSchema(name="SBER")]
