"""
FastAPI application entry point with Mangum handler for Vercel deployment.
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum

import sys
import os

# Path hack for monorepo imports: handles both local (root) and Vercel (api/ folder) execution
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
if current_dir not in sys.path:
    sys.path.append(current_dir)
if parent_dir not in sys.path and os.path.basename(current_dir) == 'api':
    sys.path.append(parent_dir)

# Import routers
try:
    from api.routers import profile, skills, projects, contact, analytics
except ImportError:
    from routers import profile, skills, projects, contact, analytics

app = FastAPI(
    title="Bhargav's Digital Resume API",
    description="FastAPI backend for digital resume showcasing AI/ML projects, research, and skills",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with your Vercel frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    """Root endpoint to verify API is running."""
    return {
        "message": "Welcome to Bhargav's Digital Resume API",
        "status": "active",
        "version": "1.0.0",
        "endpoints": {
            "profile": "/api/profile",
            "research": "/api/research",
            "education": "/api/education",
            "skills": "/api/skills",
            "projects": "/api/projects",
            "contact": "/api/contact",
            "analytics": "/api/analytics/stats"
        }
    }

@app.get("/health")
async def health_check():
    """Health check endpoint with database status."""
    import os
    db_url = os.getenv("DATABASE_URL", "NOT_SET")
    # Identify connection type without revealing credentials
    is_neon = "neon.tech" in db_url.lower()
    is_pooler = "pooler" in db_url.lower()
    return {
        "status": "healthy",
        "db_provider": "Neon" if is_neon else "Other",
        "using_pooler": is_pooler,
        "env_check": "DATABASE_URL is set" if db_url != "NOT_SET" else "DATABASE_URL is MISSING"
    }

@app.get("/debug-db")
async def debug_db(db: Session = Depends(get_db)):
    """Diagnostic endpoint to check row counts in the database."""
    try:
        from api.models import Profile, Education, Project, Research, Skill
        return {
            "profile_count": db.query(Profile).count(),
            "education_count": db.query(Education).count(),
            "project_count": db.query(Project).count(),
            "research_count": db.query(Research).count(),
            "skill_count": db.query(Skill).count(),
        }
    except Exception as e:
        return {"error": f"Database query failed: {str(e)}"}

# Register routers
app.include_router(profile.router, prefix="/api", tags=["Profile"])
app.include_router(skills.router, prefix="/api", tags=["Skills"])
app.include_router(projects.router, prefix="/api", tags=["Projects"])
app.include_router(contact.router, prefix="/api", tags=["Contact"])
app.include_router(analytics.router, prefix="/api", tags=["Analytics"])

# Mangum handler for Vercel serverless deployment
handler = Mangum(app)
