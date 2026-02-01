"""
Profile router for profile, research, and education endpoints.
"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from api.database import get_db
from api.models import Profile, Research, Education
from api.schemas import ProfileSchema, ResearchSchema, EducationSchema

router = APIRouter()


@router.get("/profile", response_model=ProfileSchema)
async def get_profile(db: Session = Depends(get_db)):
    """
    Get user profile information.
    
    Returns:
        ProfileSchema: User profile data
    """
    profile = db.query(Profile).first()
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    return profile


@router.get("/research", response_model=List[ResearchSchema])
async def get_research(db: Session = Depends(get_db)):
    """
    Get all research work.
    
    Returns:
        List[ResearchSchema]: List of research projects
    """
    research = db.query(Research).all()
    return research


@router.get("/education", response_model=List[EducationSchema])
async def get_education(db: Session = Depends(get_db)):
    """
    Get all education history.
    
    Returns:
        List[EducationSchema]: List of education records ordered by start date
    """
    education = db.query(Education).order_by(Education.start_date.desc()).all()
    return education
