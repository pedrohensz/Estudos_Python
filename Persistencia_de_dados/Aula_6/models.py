from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base

class Estudante(Base):
    __tablename__ = "estudantes"

    id = Column(
        Integer,
        primary_key=True,
        index=True   # <-- corrigido
    )

    nome = Column(
        String(100),
        nullable=False
    )

    idade = Column(Integer)


class Matricula(Base):
    __tablename__ = "matriculas"

    id = Column(
        Integer,
        primary_key=True,
        index=True   # <-- corrigido
    )

    id_estudante = Column(
        Integer,
        ForeignKey("estudantes.id"),   # <-- corrigido
        nullable=False
    )

    nome_disciplina = Column(
        String(100),
        nullable=False
    )
