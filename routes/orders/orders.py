from fastapi import APIRouter, Depends, HTTPException
from models import Pedido, PedidoItem, Usuario
from dependencies import pegar_sessao, verificar_token
from schemas import PedidoSchema, PedidoItemSchema
from sqlalchemy.orm import Session

orders_router = APIRouter(prefix="/pedidos", tags=["pedidos"], dependencies=[Depends(verificar_token)])

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

@orders_router.post('/pedido/cancelar/{pedido_id}')
async def cancelar_pedido(pedido_id: int, usuario: Usuario = Depends(verificar_token), session: Session = Depends(pegar_sessao)):    
    pedido = session.query(Pedido).filter(Pedido.id==pedido_id).first()
    if not pedido:
        raise HTTPException(status_code=400, detail="Pedido não encontrado")
    
    if not usuario.admin and usuario.id != pedido.usuario_id:
        raise HTTPException(status_code=401, detail="Você não tem autorização para fazer essa modificação")
    
    pedido.status = 'CANCELADO'
    session.commit()
    return {
        "mensagem": f"Pedido {pedido.id} cancelado com sucesso",
        "pedido": pedido
    }
    
@orders_router.get('/listar')
async def listar_pedidos(usuario: Usuario = Depends(verificar_token), session: Session = Depends(pegar_sessao)):
    if not usuario.admin:
        raise HTTPException(status_code=401, detail="Você não tem autorização para fazer essa operação")
    
    pedidos = session.query(Pedido).all()
    return {
        "pedidos": pedidos
    }
    
@orders_router.post('/pedido/adicionar-item/{pedido_id}')
async def adicionar_item_pedido(
    pedido_id: int,
    item: PedidoItemSchema, 
    usuario: Usuario = Depends(verificar_token), 
    session: Session = Depends(pegar_sessao)
):
    pedido = session.query(Pedido).filter(Pedido.id==pedido_id).first()
    if not pedido:
        raise HTTPException(status_code=400, detail="Pedido não encontrado")
    
    if not usuario.admin and usuario.id != pedido.usuario_id:
        raise HTTPException(status_code=401, detail="Você não tem autorização para fazer essa operação")
    
    pedido_item = PedidoItem(pedido_id, item.quantidade, item.sabor, item.tamanho, item.preco_unitario)
    
    session.add(pedido_item)
    
    pedido.calcular_preco()
    session.commit()
    return {
        "mensagem": "Item criado com sucesso",
        "item_id": pedido_item.id,
        "preco_pedido": pedido.preco
    }
 