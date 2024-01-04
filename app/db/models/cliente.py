from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer
from app.db.base_class import Base

class Cliente(Base):
    __tablename__ = "clientes"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)

    configuracao_cliente = relationship("ConfiguracaoCliente", back_populates="cliente")
    aprovadores_cliente = relationship("AprovadoresCliente", back_populates="cliente")
    tipos_rating_cliente = relationship("TiposRatingCliente", back_populates="cliente")
    alcadas_cliente = relationship("AlcadasCliente", back_populates="cliente")