from .auth.auth import auth_router
from .orders.orders import orders_router
from fastapi import APIRouter

web_router = APIRouter()
web_router.include_router(auth_router)
web_router.include_router(orders_router)