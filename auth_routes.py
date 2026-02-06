from fastapi import APIRouter, Depends
from models import Usuario
from dependencies import pegar_sessao
auth_router = APIRouter(prefix="/auth", tags=["Auth"])

@auth_router.get("/")
async def auth():
  """
  Rota padrão de autenticação
  """
  return {"message": "Voce acessou o AUTH"}


@auth_router.post("/criar_conta")
async def criar_conta(email: str, senha: str, nome: str, session = Depends(pegar_sessao)):
  usuario = session.query(Usuario).filter(Usuario.email==email).first()
  if usuario:
    #ja existe usuario com este email
    return {"Mensagem":"Usuario já cadastrado"}
  else: 
    novo_usuario = Usuario(nome, email, senha)
    session.add(novo_usuario)
    session.commit()
    return {"Mensagen":"Usuario cadastrado com sucesso"}
   