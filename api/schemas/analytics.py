"""
Pydantic schemas for Analytics (PageView) model.
"""
from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class PageViewCreate(BaseModel):
    """Schema for creating page view."""
    page: str
    referrer: Optional[str] = None


class PageViewSchema(PageViewCreate):
    """Schema for reading page view data."""
    id: int
    viewed_at: datetime
    
    class Config:
        from_attributes = True


class AnalyticsStats(BaseModel):
    """Schema for analytics statistics."""
    total_views: int
    unique_visitors: int
    popular_pages: dict
