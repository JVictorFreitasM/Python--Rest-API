from fastapi import APIRouter

order_router = APIRouter(prefix="/order", tags=["Order"])

@order_router.get('/')
async def order():
  """
  Rota padrão de pedidos. Todas as rotas de pedidos precisam de autenticação
  """
  return {"message": "Você acessou a rota ORDER"}
  