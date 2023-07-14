from infra.configs.connection import DBConnectionHandler
from infra.entities.aposta import Aposta


class ApostaRepository:

    # Método para realizar a consulta de todas as notas
    def select_all(self):
        with DBConnectionHandler() as db:
            data = db.query(Aposta).all()
            return data

    def select(self, id):
        with DBConnectionHandler() as db:
            data = db.query(Aposta).filter(Aposta.id == id).first()
            return data

    # Método para a inserção de notas no banco de dados
    def insert(self, nova_aposta):
        with DBConnectionHandler() as db:
            try:
                db.add(nova_aposta)
                db.commit()
                return 'Ok'
            except Exception as e:
                db.rollback()
                return e

