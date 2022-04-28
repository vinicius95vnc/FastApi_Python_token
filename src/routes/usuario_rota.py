from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.repositorios.repositorio_usuario import RepositorioUsuario
from src.schemas.schemas import Usuario
from src.infra.sqlalchemy.config.database import get_db

route = APIRouter()

# ROTA USUARIOS
@route.post('/usuarios', status_code=status.HTTP_201_CREATED, response_model=Usuario)
def cadastrar_Usuario(usuario: Usuario, db: Session = Depends(get_db)):
    usuario_cadastrado = RepositorioUsuario(db).criar(usuario)
    return usuario_cadastrado

@route.get('/usuarios', status_code=status.HTTP_200_OK)
def listar_usuarios(db: Session = Depends(get_db)):
    usuarios_listados = RepositorioUsuario(db).listar()
    return usuarios_listados

@route.put('/usuarios', response_model=Usuario)
def editar_usuario(usuario: Usuario, db: Session = Depends(get_db)):
    RepositorioUsuario(db).editar(usuario)
    return usuario

@route.delete('/usuarios/{id}')
def remover_usuario(id: int, db: Session = Depends(get_db)):
    RepositorioUsuario(db).remover(id)
    return
