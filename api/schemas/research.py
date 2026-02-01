"""
Pydantic schemas for Research model.
"""
from pydantic import BaseModel
from typing import Optional
from datetime import date


class ResearchBase(BaseModel):
    """Base research schema."""
    title: str
    description: str
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    institution: Optional[str] = None
    publication_url: Optional[str] = None
    status: Optional[str] = None


class ResearchCreate(ResearchBase):
    """Schema for creating research."""
    pass


class ResearchUpdate(BaseModel):
    """Schema for updating research."""
    title: Optional[str] = None
    description: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    institution: Optional[str] = None
    publication_url: Optional[str] = None
    status: Optional[str] = None


class ResearchSchema(ResearchBase):
    """Schema for reading research data."""
    id: int
    
    class Config:
        from_attributes = True
