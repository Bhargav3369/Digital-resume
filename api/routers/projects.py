"""
Projects router for projects endpoints.
"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from api.database import get_db
from api.models import Project
from api.schemas import ProjectSchema

router = APIRouter()


@router.get("/projects", response_model=List[ProjectSchema])
async def get_projects(
    featured: bool = None,
    db: Session = Depends(get_db)
):
    """
    Get all projects, optionally filtered by featured status.
    
    Args:
        featured: Optional filter for featured projects
        
    Returns:
        List[ProjectSchema]: List of projects
    """
    query = db.query(Project)
    
    if featured is not None:
        query = query.filter(Project.featured == featured)
    
    projects = query.order_by(Project.start_date.desc()).all()
    return projects


@router.get("/projects/{project_id}", response_model=ProjectSchema)
async def get_project(project_id: int, db: Session = Depends(get_db)):
    """
    Get a specific project by ID.
    
    Args:
        project_id: Project ID
        
    Returns:
        ProjectSchema: Project details
    """
    project = db.query(Project).filter(Project.id == project_id).first()
    
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    
    # Increment view count
    project.view_count += 1
    db.commit()
    db.refresh(project)
    
    return project
