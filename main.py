from fastapi import FastAPI
#Instancia do FastAPI
app = FastAPI()
#importando as rotas após a instancia 
from auth_routes import auth_router
from order_routes import order_router
#incluindo as rotas criadas
app.include_router(auth_router)
app.include_router(order_router)
