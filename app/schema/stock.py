from schema.base import BaseSchema


class GetStockSchema(BaseSchema):
    ticker: str
    short_name: str | None
    price: float | None
    volume: float | None


class GetStockFullSchema(GetStockSchema):
    open: float | None
    low: float | None
    high: float | None
    prev_close: float | None
    change: float | None
    change_percent: float | None
