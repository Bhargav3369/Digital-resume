"""
Pydantic schemas for Profile model.
"""
from pydantic import BaseModel, EmailStr
from typing import Optional


class ProfileBase(BaseModel):
    """Base profile schema."""
    full_name: str
    title: str
    bio: str
    email: EmailStr
    linkedin_url: Optional[str] = None
    github_url: Optional[str] = None
    twitter_url: Optional[str] = None
    location: Optional[str] = None
    phone: Optional[str] = None


class ProfileCreate(ProfileBase):
    """Schema for creating a profile."""
    pass


class ProfileUpdate(BaseModel):
    """Schema for updating a profile (all fields optional)."""
    full_name: Optional[str] = None
    title: Optional[str] = None
    bio: Optional[str] = None
    email: Optional[EmailStr] = None
    linkedin_url: Optional[str] = None
    github_url: Optional[str] = None
    twitter_url: Optional[str] = None
    location: Optional[str] = None
    phone: Optional[str] = None


class ProfileSchema(ProfileBase):
    """Schema for reading profile data."""
    id: int
    
    class Config:
        from_attributes = True
