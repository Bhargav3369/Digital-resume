"""
Pydantic schemas for Skill model.
"""
from pydantic import BaseModel
from typing import Optional


class SkillBase(BaseModel):
    """Base skill schema."""
    name: str
    category: str
    proficiency: Optional[str] = None
    order: Optional[int] = 0


class SkillCreate(SkillBase):
    """Schema for creating skill."""
    pass


class SkillUpdate(BaseModel):
    """Schema for updating skill."""
    name: Optional[str] = None
    category: Optional[str] = None
    proficiency: Optional[str] = None
    order: Optional[int] = None


class SkillSchema(SkillBase):
    """Schema for reading skill data."""
    id: int
    
    class Config:
        from_attributes = True
