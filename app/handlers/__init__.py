from handlers.start import router as start_router
from handlers.ticker import ticker_router as ticker_router

routers = [
    start_router,
    ticker_router,
]
