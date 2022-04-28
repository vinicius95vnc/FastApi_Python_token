from fastapi import APIRouter, status, Depends
from src.infra.sqlalchemy.config.database import get_db
from sqlalchemy.orm import Session
from src.schemas.schemas import Cliente
from src.infra.sqlalchemy.repositorios.repositorio_cliente import RepositorioCliente

route = APIRouter()

# ROTA CLIENTES
@route.post('/clientes', status_code=status.HTTP_201_CREATED, response_model=Cliente)
def cadastrar_cliente(cliente: Cliente, db: Session = Depends(get_db)):
    cliente_cadastrado = RepositorioCliente(db).criar(cliente)
    return cliente_cadastrado

@route.get('/clientes', status_code=status.HTTP_200_OK)
def listar_clientes(db: Session = Depends(get_db)):
    clientes = RepositorioCliente(db).listar()
    return clientes

@route.put('/clientes', response_model=Cliente)
def editar_cliente(cliente: Cliente, db: Session = Depends(get_db)):
    RepositorioCliente(db).editar(cliente)
    return cliente

@route.delete('/clientes/{id}')
def remover_cliente(id: int, db: Session = Depends(get_db)):
    RepositorioCliente(db).remover(id)
    return
