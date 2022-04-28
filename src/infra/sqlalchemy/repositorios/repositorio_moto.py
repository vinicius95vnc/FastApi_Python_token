from sqlalchemy.orm import Session
from sqlalchemy import update, delete
from src.schemas import schemas
from src.infra.sqlalchemy.models import models

class RepositorioMotos:

    def __init__(self, db: Session):
        self.db = db

    def criar(self, moto: schemas.Moto):
        db_moto = models.Moto(
            modelo=moto.modelo,
            marca=moto.marca,
            cor=moto.cor,
            observacoes=moto.observacoes)

        self.db.add(db_moto)
        self.db.commit()
        self.db.refresh(db_moto)
        return db_moto

    def listar(self):
        motos = self.db.query(models.Moto).all()
        return motos

    def editar(self, moto: schemas.Moto):
        update_db = update(models.Moto).where(models.Moto.id == moto.id).values(
            modelo=moto.modelo,
            marca=moto.marca,
            cor=moto.cor,
            observacoes=moto.observacoes)

        self.db.execute(update_db)
        self.db.commit()

    def remover(self, id: int):
        remover_db = delete(models.Moto).where(models.Moto.id == id)

        self.db.execute(remover_db)
        self.db.commit()
