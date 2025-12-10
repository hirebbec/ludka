from schema.base import BaseSchema


class GetTickerSchema(BaseSchema):
    secid: str
    short_name: str | None
    price: float | None
    volume: float | None


class GetTickerFullSchema(GetTickerSchema):
    open: float | None
    low: float | None
    high: float | None
    prev_close: float | None
    change: float | None
    change_percent: float | None
