from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from src.schemas.schemas import Moto
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repositorios.repositorio_moto import RepositorioMotos

route = APIRouter()

# ROTA MOTOS
@route.post('/motos', status_code=status.HTTP_201_CREATED, response_model=Moto)
def Cadastrar_moto(moto: Moto, db: Session = Depends(get_db)):
    moto_cadastrada = RepositorioMotos(db).criar(moto)
    return moto_cadastrada

@route.get('/motos', status_code=status.HTTP_200_OK)
def listar_motos(db: Session = Depends(get_db)):
    moto = RepositorioMotos(db).listar()
    return moto

@route.put('/motos', response_model=Moto)
def editar_moto(moto: Moto, db: Session = Depends(get_db)):
    RepositorioMotos(db).editar(moto)
    return moto

@route.delete('/motos/{id}')
def remover_moto(id: int, db: Session = Depends(get_db)):
    RepositorioMotos(db).remover(id)
    return
