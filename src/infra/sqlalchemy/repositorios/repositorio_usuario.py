from sqlalchemy.orm import Session
from sqlalchemy import update, delete
from src.schemas import schemas
from src.infra.sqlalchemy.models import models


class RepositorioUsuario:

    def __init__(self, db: Session):
        self.db = db

    def criar(self, usuario: schemas.Usuario):
        db_usuario = models.Usuario(
            nome=usuario.nome,
            senha=usuario.senha,
            contato=usuario.contato,
            email=usuario.email)

        self.db.add(db_usuario)
        self.db.commit()
        self.db.refresh(db_usuario)
        return db_usuario

    def listar(self):
        usuarios = self.db.query(models.Usuario).all()
        return usuarios

    def editar(self, usuario: schemas.Usuario):
        update_db = update(models.Usuario).where(models.Usuario.id == usuario.id).values(
            nome=usuario.nome,
            senha=usuario.senha,
            contato=usuario.contato,
            email=usuario.email)

        self.db.execute(update_db)
        self.db.commit()

    def remover(self, id: int):
        remover_db = delete(models.Usuario).where(models.Usuario.id == id)

        self.db.execute(remover_db)
        self.db.commit()
