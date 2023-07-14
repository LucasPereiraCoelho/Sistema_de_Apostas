from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from infra.configs.base import Base

class DBConnectionHandler:

    def __init__(self):
        #Dados de endereço do banco de dados
        self.__connection_string = 'mysql+pymysql://root:Senac2021@localhost:3306/aposta'

        #Instância do engine(gerenciador do banco)
        self.__engine = self.__create_database_engine()

        #Sessão nula para que possa ser instanciada uma nova ao instanciar um obj
        self.session = None

        #Validação da existência do banco de dados ao instanciar um obj
        self.__create_database()

    #Método para validação da existência do banco de dados, caso não exista
    #realiza a criação
    def __create_database(self):
        engine = create_engine(self.__connection_string, echo=True)
        try:
            engine.connect()
        except Exception as e:
            if '1049' in str(e):
                engine = create_engine(self.__connection_string.rsplit('/', 1) [0], echo=True)
                conn = engine.connect()
                conn.execute(f'CREATE DATABASE IF NOT EXISTS {self.__connection_string.rsplit("/", 1)[1]}')
                conn.close()
                print('Banco aposta criado com sucesso!')
                self.__create_table()
            else:
                raise e

    def __create_table(self):
        engine = create_engine(self.__connection_string, echo=True)
        Base.metadata.create_all(bind=engine)
        print('Tabela aposta criada com sucesso')

    #Função para a criação da engine sem necessidade de informar dados de endereço do banco
    #e utilização de querys escritos a mão
    def __create_database_engine(self):
        engine = create_engine(self.__connection_string)
        return engine

    def get_engine(self):
        return self.__engine

    #Funções mágicas que definem qualquer comportamento ao serem geradas instâncias
    def __enter__(self):
        session_make = sessionmaker(bind=self.__engine)
        self.session = session_make()
        print('Gerando conexão')
        return self.session

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Fechando conexão')
        self.session.close()