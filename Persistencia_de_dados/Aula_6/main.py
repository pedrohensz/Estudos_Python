from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models
import schemas
from database import SessionLocal, engine

#cria as tabalas no postgres (caso não existam)
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/estudantes",response_model=schemas.EstudanteResponse)
def CriarEstudante(Estudante:schemas.EstudanteCreate,db:Session=Depends(get_db)):
    db_estudante = models.Estudante(**Estudante.model_dump())
    db.add(db_estudante)
    db.commit()
    db.refresh(db_estudante)
    return db_estudante



@app.get("/estudantes", response_model=list[schemas.EstudanteResponse])
def LerEstudantes(db: Session = Depends(get_db)):
    estudantes = db.query(models.Estudante).all()
    return estudantes

@app.post("/matricula", response_model=schemas.MatriculaResponse)
def CriarMatricula(Matricula:schemas.MatriculaCreate,db:Session=Depends(get_db)):
    db_matricula = models.Matricula(**Matricula.model_dump())
    db.add(db_matricula)
    db.commit()
    db.refresh(db_matricula)
    return db_matricula

@app.get("/matricula", response_model=list[schemas.MatriculaResponse])
def LerMatriculas(db: Session = Depends(get_db)):
    matricula = db.query(models.Matricula).all()
    return matricula

@app.delete("/delete/Aluno/{id}")
def Deletar(id:int,db: Session = Depends(get_db)):
    aluno = db.get(models.Estudante, id)
    if not aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    db.delete(aluno)
    db.commit()
    return{'message': "Aluno deletado com sucesso."}