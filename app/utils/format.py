from typing import Sequence

from config import settings
from schema.subscription import GetSubscriptionSchema
from schema.stock import GetStockSchema, GetStockFullSchema


def format_stocks(stocks: Sequence[GetStockSchema]) -> str:
    lines = []

    for stock in stocks:
        lines.append(
            (
                f"📈 <b>{stock.ticker}</b> — {stock.short_name or '—'}\n"
                f"💵 Цена: {stock.price or '-'}\n"
                f"📊 Объём: {stock.volume:,}\n"
            )
        )

    text = "\n".join(lines)

    return text[: settings().TELEGRAM_MESSAGE_LEN_LIMIT]


def format_stock(ticker: GetStockFullSchema) -> str:
    return (
        f"📈 <b>{ticker.ticker}</b> — {ticker.short_name or '—'}\n"
        f"💵 Цена: {ticker.price if ticker.price is not None else '-'}\n"
        f"📊 Объём: {ticker.volume:,} \n"
        f"📤 Открытие: {ticker.open if ticker.open is not None else '-'}\n"
        f"📉 Min: {ticker.low if ticker.low is not None else '-'}\n"
        f"📈 Max: {ticker.high if ticker.high is not None else '-'}\n"
        f"💵 Цена закрытия предыдущего дня: {ticker.prev_close if ticker.prev_close is not None else '-'}\n"
        f"🔄 Изменение: {ticker.change if ticker.change is not None else '-'}\n"
        f"📐 Изм. %: {ticker.change_percent if ticker.change_percent is not None else '-'}%\n"
    )


def format_subscriptions(subscriptions: Sequence[GetSubscriptionSchema]) -> str:
    lines = []

    for subscription in subscriptions:
        lines.append(f"<b>{subscription.ticker}\n</b>")

    text = "\n".join(lines)

    return text[: settings().TELEGRAM_MESSAGE_LEN_LIMIT] if text else "Подписок нету."
