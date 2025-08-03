from fastapi import APIRouter, Depends, HTTPException
from models import Pedido
from dependencies import pegar_sessao
from schemas import PedidoSchema
from sqlalchemy.orm import Session

orders_router = APIRouter(prefix="/pedidos", tags=["pedidos"])

@orders_router.get("")
async def get_orders():
    """
    Essa é a rota padrão de pedidos do nosso sistema. Todas as rotass dos peddos precisam de
    """
    return {"message": "List of orders"}

@orders_router.post("/pedido")
async def criar_pedido(pedido_schema: PedidoSchema, session: Session = Depends(pegar_sessao)):
    """
    Cria um novo pedido no sistema.
    """
    novo_pedido = Pedido(pedido_schema.usuario_id)
    
    session.add(novo_pedido)
    session.commit()
    
    return {"message": f"Pedido criado com sucesso. ID: {novo_pedido.id} "}