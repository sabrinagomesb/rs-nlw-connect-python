from src.model.configs.base import Base
from sqlalchemy import Column, String, Integer

class Eventos(Base):
    __tablename__ = "eventos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)

