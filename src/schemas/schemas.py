from pydantic import BaseModel
from typing import Optional, List

class ClienteSimples(BaseModel):
    id: Optional[int] = None
    nome: str
    sobrenome: str
    documento: str

    class Config:
        orm_mode = True

class MotoSimples(BaseModel):
    id: Optional[int] = None
    modelo: str
    marca: str
    cor: str

class Usuario(BaseModel):
    id: Optional[str] = None
    nome: str
    senha: str
    contato: str
    email: str

    class config:
        orm_mode = True

class Moto(BaseModel):
    id: Optional[str] = None
    modelo: str
    marca: str
    cor: str
    observacoes: str

    class config:
        orm_mode = True

class Cliente(BaseModel):
    id: Optional[str] = None
    nome: str
    sobrenome: str
    documento: str
    contato: str
    email: str
    rua: str
    numero: int
    bairro: str
    cidade: str
    estado: str

    class config:
        orm_mode = True

class Produto(BaseModel):
    id: Optional[str] = None
    nome: str
    marca: str
    quantidade: int
    aplicacao: str
    observacoes: Optional[str] = 'Sem Observações'

    class config:
        orm_mode = True

class Pedido(BaseModel):
    id: Optional[str] = None
    quantidade: int
    observacoes: Optional[str] = 'Sem Observações'

    class config:
        orm_mode = True