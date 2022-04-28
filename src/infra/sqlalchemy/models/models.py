from distutils import core
from importlib.util import module_for_loader
from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from src.infra.sqlalchemy.config.database import Base

class Produto(Base):
    __tablename__ = 'produto'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    marca = Column(String)
    quantidade = Column(Integer)
    aplicacao = Column(String)
    observacoes = Column(String)

class Usuario(Base):
    __tablename__ = 'usuario'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    senha = Column(String)
    contato = Column(String)
    email = Column(String)

class Cliente(Base):
    __tablename__ = 'cliente'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    sobrenome = Column(String)
    documento = Column(String)
    contato = Column(String)
    email = Column(String)
    rua = Column(String)
    numero = Column(Integer)
    bairro = Column(String)
    cidade = Column(String)
    estado = Column(String)

    motos = relationship('Moto', back_populates='cliente')
    pedidos = relationship('Pedido', back_populates='cliente')

class Moto(Base):
    __tablename__ = 'moto'

    id = Column(Integer, primary_key=True, index=True)
    modelo = Column(String)
    marca = Column(String)
    cor = Column(String)
    observacoes = Column(String)
    cliente_id = Column(Integer, ForeignKey('cliente.id', name='fk_cliente'))

    cliente = relationship('Cliente', back_populates='motos')
    pedidos = relationship('Pedido', back_populates='moto')

class Pedido(Base):
    __tablename__ = 'pedido'

    id = Column(Integer, primary_key=True, index=True)
    quantidade = Column(Integer)
    observacoes = Column(String)
    cliente_id = Column(Integer, ForeignKey('cliente.id', name='fk_cliente'))
    moto_id = Column(Integer, ForeignKey('moto.id', name='fk_moto'))

    cliente = relationship('Cliente', back_populates='pedidos')
    moto = relationship('Moto', back_populates='pedidos')

