# Core business logic for drug scoring
from typing import List
from . import models, database
from sqlalchemy.orm import Session

# Simple scoring algorithm: count of hetero atoms in formula
import re

def score_drug(formula: str) -> float:
    hetero = re.findall(r"[O,N,S]", formula)
    return float(len(hetero))

# Update drug scores in batch
def update_drug_scores(db: Session):
    drugs = db.query(models.Drug).all()
    for drug in drugs:
        drug.score = score_drug(drug.formula)
    db.commit()

# Example: compute score for a new drug
# def create_drug_with_score(drug_data: dict, db: Session):
#     drug = models.Drug(**drug_data)
#     drug.score = score_drug(drug.formula)
#     db.add(drug)
#     db.commit()
#     db.refresh(drug)
#     return drug
