from handler.start import router as start_router
from handler.stock import router as ticker_router
from handler.subscription import router as subscription_router

routers = [
    start_router,
    ticker_router,
    subscription_router,
]
