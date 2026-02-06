from sqlalchemy.orm import sessionmaker
from models import db
#criando uma função para abrir e fechar sessão no banco de dados (usarei em todas as rotas)
def pegar_sessao():
  try:
    Session = sessionmaker(bind=db)
    session = Session()
    #yield serve para obrigar a função continuar sua execução, mesmo após o return da função
    yield session
  finally:
    #independente de erro ou não, a sessão é finalizada.
    session.close()