from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Drug(Base):
    __tablename__ = "drugs"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    formula = Column(String, nullable=False)
    score = Column(Float, nullable=True)
    created_at = Column(Date, nullable=False)

    # Relationships
    clinical_trials = relationship("ClinicalTrial", back_populates="drug")

class ClinicalTrial(Base):
    __tablename__ = "clinical_trials"
    id = Column(Integer, primary_key=True, index=True)
    drug_id = Column(Integer, ForeignKey("drugs.id"), nullable=False)
    phase = Column(String, nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=True)
    outcome = Column(String, nullable=True)

    drug = relationship("Drug", back_populates="clinical_trials")
