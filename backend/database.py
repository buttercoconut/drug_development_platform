"""Database configuration using SQLAlchemy and PostgreSQL."""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql+asyncpg://postgres:postgres@localhost:5432/drug_dev"

engine = create_engine(DATABASE_URL, echo=False, future=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependency for DB session
async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
