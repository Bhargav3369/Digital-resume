"""
Pydantic schemas for Contact model.
"""
from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


class ContactCreate(BaseModel):
    """Schema for creating contact submission."""
    name: str
    email: EmailStr
    subject: Optional[str] = None
    message: str


class ContactSchema(ContactCreate):
    """Schema for reading contact data."""
    id: int
    submitted_at: datetime
    
    class Config:
        from_attributes = True
