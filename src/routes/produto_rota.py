from fastapi import APIRouter, Depends, status
from src.infra.sqlalchemy.config.database import get_db
from src.schemas.schemas import Produto
from src.infra.sqlalchemy.repositorios.repositorio_produto import RepositorioProduto
from sqlalchemy.orm import Session

route = APIRouter()

# ROTA PRODUTOS
@route.post('/produtos', status_code=status.HTTP_201_CREATED, response_model=Produto)
def criar_produto(produto: Produto, db: Session = Depends(get_db)):
    produto_criado = RepositorioProduto(db).criar(produto)
    return produto_criado

@route.get('/produtos', status_code=status.HTTP_200_OK)
def listar_produtos(db: Session = Depends(get_db)):
    produtos = RepositorioProduto(db).listar()
    return produtos

@route.put('/produtos', response_model=Produto)
def editar_produto(produto: Produto, db: Session = Depends(get_db)):
    RepositorioProduto(db).editar(produto)
    return produto

@route.delete('/produtos/{id}')
def remover_produto(id: int, db: Session = Depends(get_db)):
    RepositorioProduto(db).remover(id)
    return
