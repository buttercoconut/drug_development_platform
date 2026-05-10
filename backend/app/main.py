from fastapi import FastAPI
from .routers import drug_router, clinical_router

app = FastAPI(title="Drug Development Platform API")

# Include routers
app.include_router(drug_router, prefix="/api/drugs", tags=["drugs"])
app.include_router(clinical_router, prefix="/api/clinical", tags=["clinical"])

# Root endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to the Drug Development Platform API"}
