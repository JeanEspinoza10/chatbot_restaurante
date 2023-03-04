from app.models.base import BaseModel
from sqlalchemy import Column, String, Boolean, Integer, ForeignKey
from sqlalchemy.orm import relationship

class PedidoModel(BaseModel):
    __tablename__= "pedidos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    users = relationship("UserModel", uselist=False, back_populates="userpedido")

    menu_id = Column(Integer, ForeignKey('menu.id'))
    menus = relationship('Menu', uselist=False, back_populates='pedidos')
    direccion = Column(String(120))
    # Pago id
    # Esta columna es para ver si un pedido esta en proceso, enviado o cancelado.
    estado = Column(String(120), default="En proceso")

