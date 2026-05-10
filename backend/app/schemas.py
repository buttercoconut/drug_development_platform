from pydantic import BaseModel, Field
from datetime import date

class DrugBase(BaseModel):
    name: str = Field(..., example="Aspirin")
    formula: str = Field(..., example="C9H8O4")
    created_at: date = Field(..., example="2024-01-01")

class DrugCreate(DrugBase):
    pass

class DrugRead(DrugBase):
    id: int
    score: float | None

    class Config:
        orm_mode = True

class ClinicalTrialBase(BaseModel):
    phase: str = Field(..., example="Phase 3")
    start_date: date = Field(..., example="2024-06-01")
    end_date: date | None = None
    outcome: str | None = None

class ClinicalTrialCreate(ClinicalTrialBase):
    drug_id: int

class ClinicalTrialRead(ClinicalTrialBase):
    id: int
    drug_id: int

    class Config:
        orm_mode = True
