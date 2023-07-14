from infra.configs.base import Base
from sqlalchemy import Column, String, Integer, Float


class Aposta(Base):
        __tablename__ = 'APOSTA'

        id = Column(Integer, autoincrement=True, primary_key=True)
        nome_apostador = Column(String(100), nullable=True)
        vencedor = Column(String(length=1), nullable=True)
        time_casa = Column(Integer, nullable=True)
        time_visitante = Column(Integer, nullable=True)
        valor_aposta = Column(Integer, nullable=True)

        #Função que sobrescreve a maneira de 'printar' o objeto
        def __repr__(self):
            return f'Título da nota = {self.nome_apostador}, id = {self.id}'