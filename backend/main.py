"""FastAPI application entry point for Drug Development Platform."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .routers import drug, clinical_trial, user

app = FastAPI(title="Drug Development Platform API", version="0.1.0")

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(drug.router, prefix="/api/drugs", tags=["drugs"])
app.include_router(clinical_trial.router, prefix="/api/clinical-trials", tags=["clinical_trials"])
app.include_router(user.router, prefix="/api/users", tags=["users"])

@app.get("/health")
async def health_check():
    return {"status": "ok"}
