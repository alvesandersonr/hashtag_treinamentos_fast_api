from models.base import Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey

class PedidoItem(Base):
    __tablename__ = "pedido_itens"
    
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    pedido_id = Column("pedido_id", ForeignKey("pedidos.id"))
    quantidade = Column("quantidade", Integer, nullable=False)
    sabor = Column("sabor", String, nullable=False)
    tamanho = Column("tamanho", String, nullable=False)
    preco_unitario = Column("preco_unitario", Float, nullable=False)

    def __init__(self, pedido_id, quantidade, sabor, tamanho, preco_unitario):
        self.pedido_id = pedido_id        
        self.quantidade = quantidade
        self.sabor = sabor
        self.tamanho = tamanho
        self.preco_unitario = preco_unitario