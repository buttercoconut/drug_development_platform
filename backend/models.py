"""Domain models for the drug development platform."""

from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date, JSON
from sqlalchemy.orm import relationship

from .database import Base

class Drug(Base):
    __tablename__ = "drugs"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    formula = Column(String, nullable=True)
    score = Column(Float, nullable=True)
    created_at = Column(Date, nullable=False)

    # Relationships
    trials = relationship("ClinicalTrial", back_populates="drug")

class ClinicalTrial(Base):
    __tablename__ = "clinical_trials"
    id = Column(Integer, primary_key=True, index=True)
    drug_id = Column(Integer, ForeignKey("drugs.id"), nullable=False)
    phase = Column(String, nullable=False)
    status = Column(String, nullable=False)
    start_date = Column(Date, nullable=True)
    end_date = Column(Date, nullable=True)
    data = Column(JSON, nullable=True)

    drug = relationship("Drug", back_populates="trials")

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(String, nullable=False)
