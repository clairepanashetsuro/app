import os

from sqlalchemy import create_engine  # type: ignore[reportMissingImports]
from sqlalchemy.orm import declarative_base, sessionmaker  # type: ignore[reportMissingImports]


DATABASE_URL = "postgresql://postgres:YOUR_PASSWORD@localhost:5432/pos_db"

#  the database engine
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency to get the database session  routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
