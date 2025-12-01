from pydantic import BaseModel
from typing import List, Optional

class Perfil(BaseModel):
    id:int  
    idade:int
    endereco:str

    class Config:
        from_attributes = True

class PerfilCreate(BaseModel):
    idade: int
    endereco: str

class Estudantes(BaseModel):
    id: int
    nome: str
    email: str
    perfil: Optional[Perfil] = None

    class Config:
        from_attributes = True


class EstudanteCreate(BaseModel):
    nome: str
    email: str
    perfil: PerfilCreate