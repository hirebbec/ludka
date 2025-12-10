from typing import Sequence

from config import settings
from schema.ticker import GetTickerSchema, GetTickerFullSchema


def format_ticker_list(tickers: Sequence[GetTickerSchema]) -> str:
    lines = []

    for ticker in tickers:
        lines.append(
            (
                f"📈 <b>{ticker.secid}</b> — {ticker.short_name or '—'}\n"
                f"💵 Цена: {ticker.price or '-'}\n"
                f"📊 Объём: {ticker.volume:,}\n"
            )
        )

    text = "\n".join(lines)

    return text[: settings().TELEGRAM_MESSAGE_LEN_LIMIT]


def format_ticker(ticker: GetTickerFullSchema) -> str:
    return (
        f"📈 <b>{ticker.secid}</b> — {ticker.short_name or '—'}\n"
        f"💵 Цена: {ticker.price if ticker.price is not None else '-'}\n"
        f"📊 Объём: {ticker.volume:,} \n"
        f"📤 Открытие: {ticker.open if ticker.open is not None else '-'}\n"
        f"📉 Min: {ticker.low if ticker.low is not None else '-'}\n"
        f"📈 Max: {ticker.high if ticker.high is not None else '-'}\n"
        f"💵 Цена закрытия предыдущего дня: {ticker.prev_close if ticker.prev_close is not None else '-'}\n"
        f"🔄 Изменение: {ticker.change if ticker.change is not None else '-'}\n"
        f"📐 Изм. %: {ticker.change_percent if ticker.change_percent is not None else '-'}%\n"
    )
