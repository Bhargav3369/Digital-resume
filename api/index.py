import sys
import os

# Ensure the 'api' directory is in the path for reliable imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from api.database import get_db

# Use explicit imports for routers to avoid path issues
from api.routers import profile, skills, projects, contact, analytics

app = FastAPI(
    title="Bhargav's Digital Resume API",
    description="FastAPI backend for digital resume showcasing AI/ML projects, research, and skills",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api")
async def root():
    return {"message": "Welcome to Bhargav's Digital Resume API"}

@app.get("/api/health")
async def health_check():
    db_url = os.getenv("DATABASE_URL", "NOT_SET")
    return {
        "status": "healthy",
        "database_configured": db_url != "NOT_SET",
        "provider": "Neon" if "neon.tech" in db_url.lower() else "Unknown"
    }

@app.get("/api/debug-db")
async def debug_db(db: Session = Depends(get_db)):
    try:
        from api.models import Profile, Education, Project, Research, Skill
        return {
            "profile": db.query(Profile).count(),
            "education": db.query(Education).count(),
            "projects": db.query(Project).count(),
            "research": db.query(Research).count(),
            "skills": db.query(Skill).count(),
        }
    except Exception as e:
        return {"error": str(e)}

# Register routers
app.include_router(profile.router, prefix="/api", tags=["Profile"])
app.include_router(skills.router, prefix="/api", tags=["Skills"])
app.include_router(projects.router, prefix="/api", tags=["Projects"])
app.include_router(contact.router, prefix="/api", tags=["Contact"])
app.include_router(analytics.router, prefix="/api", tags=["Analytics"])
