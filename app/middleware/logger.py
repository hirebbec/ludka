import logging


logging.basicConfig(
    level=logging.INFO, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)

from aiogram import BaseMiddleware
from aiogram.types import Message, CallbackQuery, Update
from typing import Any, Callable, Dict, Awaitable

logger = logging.getLogger(__name__)


class LoggingMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Any, Dict[str, Any]], Awaitable[Any]],
        event: Any,
        data: Dict[str, Any],
    ):
        if isinstance(event, Message) and event.from_user:
            logger.info(f"[MESSAGE] From={event.from_user.id} Text={event.text!r}")

        elif isinstance(event, CallbackQuery) and event.from_user:
            logger.info(f"[CALLBACK] From={event.from_user.id} Data={event.data!r}")

        elif isinstance(event, Update):
            logger.info(f"[UPDATE] Raw update type={event.event_type}")

        result = await handler(event, data)

        handler_name = self.get_handler_name(handler)

        logger.info(f"[HANDLER DONE] {handler_name} for {type(event).__name__}")

        return result

    def get_handler_name(self, handler):
        if hasattr(handler, "__name__"):
            return handler.__name__

        if hasattr(handler, "func"):
            return getattr(handler.func, "__name__", str(handler))

        return str(handler)
