from sqlalchemy.orm import Session
from sqlalchemy import update, delete
from src.schemas import schemas
from src.infra.sqlalchemy.models import models


class RepositorioCliente:

    def __init__(self, db: Session):
        self.db = db

    def criar(self, cliente: schemas.Cliente):
        db_cliente = models.Cliente(
            nome=cliente.nome,
            sobrenome=cliente.sobrenome,
            documento=cliente.documento,
            contato=cliente.contato,
            email=cliente.email,
            rua=cliente.rua,
            bairro=cliente.bairro,
            numero=cliente.numero,
            cidade=cliente.cidade,
            estado=cliente.estado)

        self.db.add(db_cliente)
        self.db.commit()
        self.db.refresh(db_cliente)
        return db_cliente

    def listar(self):
        clientes = self.db.query(models.Cliente).all()
        return clientes

    def editar(self, cliente: schemas.Cliente):
        update_db = update(models.Cliente).where(models.Cliente.id == cliente.id).values(
            nome=cliente.nome,
            sobrenome=cliente.sobrenome,
            documento=cliente.documento,
            contato=cliente.contato,
            email=cliente.email,
            rua=cliente.rua,
            bairro=cliente.bairro,
            numero=cliente.numero,
            cidade=cliente.cidade,
            estado=cliente.estado)

        self.db.execute(update_db)
        self.db.commit()

    def remover(self, id: int):
        remover_db = delete(models.Cliente).where(models.Cliente.id == id)

        self.db.execute(remover_db)
        self.db.commit()
