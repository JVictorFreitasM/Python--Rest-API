from fastapi import APIRouter

auth_router = APIRouter(prefix="/auth", tags=["Auth"])

@auth_router.get("/")
async def auth():
  """
  Rota padrão de autenticação
  """
  return {"message": "Voce acessou o AUTH"}