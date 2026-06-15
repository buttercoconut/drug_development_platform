"""CRUD operations for drugs and clinical trials."""

from sqlalchemy.orm import Session
from . import models, schemas

# Drug CRUD

def create_drug(db: Session, drug: schemas.DrugCreate):
    db_drug = models.Drug(**drug.dict())
    db.add(db_drug)
    db.commit()
    db.refresh(db_drug)
    return db_drug

def get_drug(db: Session, drug_id: int):
    return db.query(models.Drug).filter(models.Drug.id == drug_id).first()

def get_drugs(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Drug).offset(skip).limit(limit).all()

# ClinicalTrial CRUD

def create_trial(db: Session, trial: schemas.ClinicalTrialCreate):
    db_trial = models.ClinicalTrial(**trial.dict())
    db.add(db_trial)
    db.commit()
    db.refresh(db_trial)
    return db_trial

def get_trial(db: Session, trial_id: int):
    return db.query(models.ClinicalTrial).filter(models.ClinicalTrial.id == trial_id).first()

# Additional functions can be added as needed
