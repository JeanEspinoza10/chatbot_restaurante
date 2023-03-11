from app.models.base import BaseModel
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, Date
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

class Menu(BaseModel):
    __tablename__ = "menu"
    # Componentes de nuestra tabla
    id = Column(Integer, primary_key=True, autoincrement=True)
    name =Column(String(120))
    precio = Column(Integer)
    fecha = Column(Date, default=func.now())
    disonibilidad = Column(Boolean, default=True)
    detalle = Column(String(250))
    pedidos = relationship('PedidoModel', back_populates='menus', uselist= True)
    
    # Añadir un modelo que relacione la categoria independiente
    categoria_id = Column(Integer,ForeignKey("categoria.id"))
    categoria = relationship("Categoria", uselist=False, back_populates='menu')