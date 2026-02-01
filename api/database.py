"""
Database configuration and session management.
"""
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get database URL from environment, default to local SQLite for development
DATABASE_URL = os.getenv("DATABASE_URL")

# If no DATABASE_URL is provided, use a local SQLite file
if not DATABASE_URL:
    DATABASE_URL = "sqlite:///./resume_local.db"
    print("WARNING: DATABASE_URL not set. Using local SQLite: resume_local.db")

# Create SQLAlchemy engine
# connect_args={"check_same_thread": False} is only needed for SQLite
connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}

engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=not DATABASE_URL.startswith("sqlite"),
    pool_recycle=300,
    connect_args=connect_args
)

# Create SessionLocal class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create Base class for models
Base = declarative_base()

# Dependency to get database session
def get_db():
    """
    Dependency function to get database session.
    Yields a database session and closes it after use.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
