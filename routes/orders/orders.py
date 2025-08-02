from fastapi import APIRouter

orders_router = APIRouter(prefix="/pedidos6.+", tags=["pedidos6.+"])

@orders_router.get("")
async def get_orders():
    """
    Essa é a rota padrão de pedidos do nosso sistema. Todas as rotass dos peddos precisam de
    """
    return {"message": "List of orders"}