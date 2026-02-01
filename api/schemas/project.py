"""
Pydantic schemas for Project model.
"""
from pydantic import BaseModel
from typing import Optional
from datetime import date


class ProjectBase(BaseModel):
    """Base project schema."""
    title: str
    description: str
    tech_stack: str
    github_url: Optional[str] = None
    live_url: Optional[str] = None
    image_url: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    featured: Optional[bool] = False


class ProjectCreate(ProjectBase):
    """Schema for creating project."""
    pass


class ProjectUpdate(BaseModel):
    """Schema for updating project."""
    title: Optional[str] = None
    description: Optional[str] = None
    tech_stack: Optional[str] = None
    github_url: Optional[str] = None
    live_url: Optional[str] = None
    image_url: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    featured: Optional[bool] = None


class ProjectSchema(ProjectBase):
    """Schema for reading project data."""
    id: int
    view_count: int = 0
    
    class Config:
        from_attributes = True
