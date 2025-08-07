from models.base import Base
from sqlalchemy import Column, Integer, Float, ForeignKey, String
from sqlalchemy.orm import relationship

class Pedido(Base):
    __tablename__ = "pedidos"
    
    # STATUS_PEDIDO = (
    #     ("PENDENTE", "PENDENTE"),
    #     ("CANCELADO", "CANCELADO"),
    #     ("FINALIZADO", "FINALIZADO"),
    # )
    
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    usuario_id = Column("usuario_id", ForeignKey("usuarios.id"), nullable=False)
    # status = Column("status", ChoiceType(STATUS_PEDIDO), nullable=False, default="PENDENTE")
    status = Column("status", String, nullable=False, default="PENDENTE")
    preco = Column("preco", Float, nullable=False)
    itens = relationship("PedidoItem", cascade="all, delete")
    
    def __init__(self, usuario_id, status="PENDENTE", preco=0):
        self.status = status
        self.usuario_id = usuario_id
        self.preco = preco
        
    def calcular_preco(self):
        preco_pedido = 0
        for item in self.itens:
            preco_item = item.preco_unitario * item.quantidade
            preco_pedido += preco_item
        
        
        self.preco = preco_pedido