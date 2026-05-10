from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from . import models, schemas, database

router = APIRouter()

# Drug endpoints
@router.post("/", response_model=schemas.DrugRead)
def create_drug(drug: schemas.DrugCreate, db: Session = Depends(database.get_db)):
    db_drug = models.Drug(**drug.dict())
    db.add(db_drug)
    db.commit()
    db.refresh(db_drug)
    return db_drug

@router.get("/", response_model=list[schemas.DrugRead])
def read_drugs(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    drugs = db.query(models.Drug).offset(skip).limit(limit).all()
    return drugs

# Clinical trial endpoints
@router.post("/trials/", response_model=schemas.ClinicalTrialRead)
def create_trial(trial: schemas.ClinicalTrialCreate, db: Session = Depends(database.get_db)):
    db_trial = models.ClinicalTrial(**trial.dict())
    db.add(db_trial)
    db.commit()
    db.refresh(db_trial)
    return db_trial

@router.get("/trials/", response_model=list[schemas.ClinicalTrialRead])
def read_trials(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    trials = db.query(models.ClinicalTrial).offset(skip).limit(limit).all()
    return trials
