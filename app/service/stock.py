import httpx

from config import settings
from schema.stock import GetStockSchema, GetStockFullSchema
from service.base import BaseService


class StockService(BaseService):
    async def get_all(self, limit: int = 30) -> list[GetStockSchema]:
        async with httpx.AsyncClient(timeout=10) as client:
            resp = await client.get(
                f"{settings().MOEX_BASE_URL}"
                f"/engines/stock/markets/shares/securities.json?iss.only=securities,marketdata"
            )

        data = resp.json()

        sec_columns = data["securities"]["columns"]
        sec_rows = data["securities"]["data"]
        secid_idx = sec_columns.index("SECID")
        shortname_idx = sec_columns.index("SHORTNAME")

        md_columns = data["marketdata"]["columns"]
        md_rows = data["marketdata"]["data"]
        md_secid_idx = md_columns.index("SECID")
        md_price_idx = md_columns.index("LAST")
        md_volume_idx = md_columns.index("VALTODAY")

        info_map: dict[str, GetStockSchema] = {}

        for row in sec_rows:
            secid = row[secid_idx]
            if secid:
                info_map[secid] = GetStockSchema(
                    ticker=secid,
                    short_name=row[shortname_idx],
                    price=None,
                    volume=None,
                )

        for row in md_rows:
            secid = row[md_secid_idx]
            if secid in info_map:
                info_map[secid].price = row[md_price_idx] or 0
                info_map[secid].volume = row[md_volume_idx] or 0

        tickers = list(info_map.values())

        tickers.sort(key=lambda x: x.volume or 0, reverse=True)

        return tickers[:limit]

    async def get_by_ticker(self, ticker: str) -> GetStockFullSchema | None:
        url = (
            f"{settings().MOEX_BASE_URL}"
            f"/engines/stock/markets/shares/boards/TQBR/securities/{ticker}.json"
        )

        async with httpx.AsyncClient(timeout=10) as client:
            resp = await client.get(url)

        data = resp.json()

        sec_cols = data["securities"]["columns"]
        sec_data = data["securities"]["data"]

        if not sec_data:
            return None

        sec_row = sec_data[0]

        get_sec = (
            lambda name: sec_row[sec_cols.index(name)] if name in sec_cols else None
        )

        md_cols = data["marketdata"]["columns"]
        md_data = data["marketdata"]["data"]

        price = md_data[0][md_cols.index("LAST")]
        prev_close = sec_row[sec_cols.index("PREVPRICE")]

        change = round(price - prev_close, 2)
        change_percent = round((change / prev_close * 100), 2)

        return GetStockFullSchema(
            ticker=ticker,
            short_name=get_sec("SHORTNAME"),
            price=price,
            volume=md_data[0][md_cols.index("VALTODAY")],
            open=md_data[0][md_cols.index("OPEN")],
            low=md_data[0][md_cols.index("LOW")],
            high=md_data[0][md_cols.index("HIGH")],
            prev_close=prev_close,
            change=change,
            change_percent=change_percent,
        )
