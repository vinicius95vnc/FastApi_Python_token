from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, status
from src.schemas.schemas import Produto, Cliente, Usuario, Moto
from src.infra.sqlalchemy.config.database import get_db, criar_bd
from fastapi.middleware.cors import CORSMiddleware
from src.infra.sqlalchemy.repositorios.repositorio_produto import RepositorioProduto
from src.infra.sqlalchemy.repositorios.repositorio_cliente import RepositorioCliente
from src.infra.sqlalchemy.repositorios.repositorio_usuario import RepositorioUsuario
from src.infra.sqlalchemy.repositorios.repositorio_moto import RepositorioMotos

criar_bd()

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

# ROTA CLIENTES
@app.post('/clientes', status_code=status.HTTP_201_CREATED, response_model=Cliente)
def cadastrar_cliente(cliente: Cliente, db: Session = Depends(get_db)):
    cliente_cadastrado = RepositorioCliente(db).criar(cliente)
    return cliente_cadastrado

@app.get('/clientes', status_code=status.HTTP_200_OK)
def listar_clientes(db: Session = Depends(get_db)):
    clientes = RepositorioCliente(db).listar()
    return clientes

@app.put('/clientes', response_model=Cliente)
def editar_cliente(cliente: Cliente, db: Session = Depends(get_db)):
    RepositorioCliente(db).editar(cliente)
    return cliente

@app.delete('/clientes/{id}')
def remover_cliente(id: int, db: Session = Depends(get_db)):
    RepositorioCliente(db).remover(id)
    return

# ROTA USUARIOS
@app.post('/usuarios', status_code=status.HTTP_201_CREATED, response_model=Usuario)
def cadastrar_Usuario(usuario: Usuario, db: Session = Depends(get_db)):
    usuario_cadastrado = RepositorioUsuario(db).criar(usuario)
    return usuario_cadastrado

@app.get('/usuarios', status_code=status.HTTP_200_OK)
def listar_usuarios(db: Session = Depends(get_db)):
    usuarios_listados = RepositorioUsuario(db).listar()
    return usuarios_listados

@app.put('/usuarios', response_model=Usuario)
def editar_usuario(usuario: Usuario, db: Session = Depends(get_db)):
    RepositorioUsuario(db).editar(usuario)
    return usuario

@app.delete('/usuarios/{id}')
def remover_usuario(id: int, db: Session = Depends(get_db)):
    RepositorioUsuario(db).remover(id)
    return

# ROTA PRODUTOS
@app.post('/produtos', status_code=status.HTTP_201_CREATED, response_model=Produto)
def criar_produto(produto: Produto, db: Session = Depends(get_db)):
    produto_criado = RepositorioProduto(db).criar(produto)
    return produto_criado

@app.get('/produtos', status_code=status.HTTP_200_OK)
def listar_produtos(db: Session = Depends(get_db)):
    produtos = RepositorioProduto(db).listar()
    return produtos

@app.put('/produtos', response_model=Produto)
def editar_produto(produto: Produto, db: Session = Depends(get_db)):
    RepositorioProduto(db).editar(produto)
    return produto

@app.delete('/produtos/{id}')
def remover_produto(id: int, db: Session = Depends(get_db)):
    RepositorioProduto(db).remover(id)
    return

# ROTA MOTOS
@app.post('/motos', status_code=status.HTTP_201_CREATED, response_model=Moto)
def Cadastrar_moto(moto: Moto, db: Session = Depends(get_db)):
    moto_cadastrada = RepositorioMotos(db).criar(moto)
    return moto_cadastrada

@app.get('/motos', status_code=status.HTTP_200_OK)
def listar_motos(db: Session = Depends(get_db)):
    moto = RepositorioMotos(db).listar()
    return moto

@app.put('/motos', response_model=Moto)
def editar_moto(moto: Moto, db: Session = Depends(get_db)):
    RepositorioMotos(db).editar(moto)
    return moto

@app.delete('/motos/{id}')
def remover_moto(id: int, db: Session = Depends(get_db)):
    RepositorioMotos(db).remover(id)
    return
