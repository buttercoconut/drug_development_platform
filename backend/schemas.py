"""Pydantic schemas for request/response validation."""

from datetime import date
from typing import List, Optional

from pydantic import BaseModel, Field

class DrugBase(BaseModel):
    name: str = Field(..., example="Aspirin")
    formula: Optional[str] = Field(None, example="C9H8O4")
    score: Optional[float] = Field(None, example=0.85)
    created_at: date = Field(..., example="2024-01-01")

class DrugCreate(DrugBase):
    pass

class DrugRead(DrugBase):
    id: int

    class Config:
        orm_mode = True

class ClinicalTrialBase(BaseModel):
    drug_id: int
    phase: str
    status: str
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    data: Optional[dict] = None

class ClinicalTrialCreate(ClinicalTrialBase):
    pass

class ClinicalTrialRead(ClinicalTrialBase):
    id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str
    role: str

class UserRead(UserBase):
    id: int
    role: str

    class Config:
        orm_mode = True
