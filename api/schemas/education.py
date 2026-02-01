"""
Pydantic schemas for Education model.
"""
from pydantic import BaseModel
from typing import Optional
from datetime import date


class EducationBase(BaseModel):
    """Base education schema."""
    degree: str
    institution: str
    location: Optional[str] = None
    start_date: date
    end_date: Optional[date] = None
    gpa: Optional[float] = None
    description: Optional[str] = None
    achievements: Optional[str] = None


class EducationCreate(EducationBase):
    """Schema for creating education."""
    pass


class EducationUpdate(BaseModel):
    """Schema for updating education."""
    degree: Optional[str] = None
    institution: Optional[str] = None
    location: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    gpa: Optional[float] = None
    description: Optional[str] = None
    achievements: Optional[str] = None


class EducationSchema(EducationBase):
    """Schema for reading education data."""
    id: int
    
    class Config:
        from_attributes = True
