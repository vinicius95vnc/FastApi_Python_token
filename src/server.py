from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routes import moto_rota, cliente_rota, usuario_rota, produto_rota


app = FastAPI()

# CORS conexão
origins = ['http://localhost:3000',
           'http://lojagarage70s.com',
           'http://lojagarage70s.com.br']

app.add_middleware(CORSMiddleware,
                   allow_origins=origins,
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"],)

# ROTAS PRODUTOS
app.include_router(produto_rota.route)
# ROTAS USUARIO
app.include_router(usuario_rota.route)
# ROTAS CLIENTE
app.include_router(cliente_rota.route)
# ROTAS MOTO
app.include_router(moto_rota.route)