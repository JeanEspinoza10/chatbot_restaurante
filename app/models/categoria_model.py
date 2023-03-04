from app.models.base import BaseModel
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, Date
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

class Categoria(BaseModel):
    __tablename__ ="categoria"

    # Columnas
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(120))
    status = Column(Boolean, default=True)
    
    menu = relationship("Menu", uselist=True, back_populates='categoria')
