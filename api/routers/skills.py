"""
Skills router for skills endpoints.
"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Dict
from collections import defaultdict

from api.database import get_db
from api.models import Skill
from api.schemas import SkillSchema

router = APIRouter()


@router.get("/skills", response_model=List[SkillSchema])
async def get_skills(
    category: str = None,
    db: Session = Depends(get_db)
):
    """
    Get all skills, optionally filtered by category.
    
    Args:
        category: Optional category filter
        
    Returns:
        List[SkillSchema]: List of skills ordered by category and order
    """
    query = db.query(Skill)
    
    if category:
        query = query.filter(Skill.category == category)
    
    skills = query.order_by(Skill.category, Skill.order).all()
    return skills


@router.get("/skills/grouped")
async def get_skills_grouped(db: Session = Depends(get_db)):
    """
    Get skills grouped by category.
    
    Returns:
        Dict: Skills grouped by category
    """
    skills = db.query(Skill).order_by(Skill.category, Skill.order).all()
    
    grouped = defaultdict(list)
    for skill in skills:
        grouped[skill.category].append({
            "id": skill.id,
            "name": skill.name,
            "proficiency": skill.proficiency,
            "order": skill.order
        })
    
    return dict(grouped)
