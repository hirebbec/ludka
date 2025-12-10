from handler.start import router as start_router
from handler.ticker import ticker_router as ticker_router

routers = [
    start_router,
    ticker_router,
]
