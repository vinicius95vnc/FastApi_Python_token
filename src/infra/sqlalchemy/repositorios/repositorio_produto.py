from sqlalchemy.orm import Session
from sqlalchemy import update, delete
from src.schemas import schemas
from src.infra.sqlalchemy.models import models


class RepositorioProduto:
    
    def __init__(self, db: Session):
        self.db = db

    def criar(self, produto: schemas.Produto):
        db_produto = models.Produto(
            nome=produto.nome,
            marca=produto.marca,
            quantidade=produto.quantidade,
            aplicacao=produto.aplicacao,
            observacoes=produto.observacoes)

        self.db.add(db_produto)
        self.db.commit()
        self.db.refresh(db_produto)
        return db_produto

    def listar(self):
        produtos = self.db.query(models.Produto).all()
        return produtos

    def editar(self, produto: schemas.Produto):
        update_db = update(models.Produto).where(models.Produto.id == produto.id).values(
            nome=produto.nome,
            marca=produto.marca,
            quantidade=produto.quantidade,
            aplicacao=produto.aplicacao,
            observacoes=produto.observacoes)

        self.db.execute(update_db)
        self.db.commit()

    def remover(self, id: int):
        remover_db = delete(models.Produto).where(models.Produto.id == id)

        self.db.execute(remover_db)
        self.db.commit()
