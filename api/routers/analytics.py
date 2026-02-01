"""
Analytics router for page view tracking and statistics.
"""
from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import datetime, timedelta

from api.database import get_db
from api.models import PageView
from api.schemas import PageViewCreate, PageViewSchema, AnalyticsStats

router = APIRouter()


@router.post("/analytics/pageview", response_model=PageViewSchema, status_code=201)
async def track_page_view(
    pageview_data: PageViewCreate,
    request: Request,
    db: Session = Depends(get_db)
):
    """
    Track a page view.
    
    Args:
        pageview_data: Page view data
        request: FastAPI request object
        
    Returns:
        PageViewSchema: Created page view record
    """
    # Get client info
    client_ip = request.client.host if request.client else "unknown"
    user_agent = request.headers.get("user-agent", "")
    
    # Create page view record
    pageview = PageView(
        page=pageview_data.page,
        ip_address=client_ip,
        user_agent=user_agent,
        referrer=pageview_data.referrer
    )
    
    db.add(pageview)
    db.commit()
    db.refresh(pageview)
    
    return pageview


@router.get("/analytics/stats", response_model=AnalyticsStats)
async def get_analytics_stats(
    days: int = 30,
    db: Session = Depends(get_db)
):
    """
    Get analytics statistics.
    
    Args:
        days: Number of days to analyze (default: 30)
        
    Returns:
        AnalyticsStats: Analytics statistics
    """
    since_date = datetime.utcnow() - timedelta(days=days)
    
    # Total views
    total_views = db.query(func.count(PageView.id)).filter(
        PageView.viewed_at >= since_date
    ).scalar()
    
    # Unique visitors (based on IP)
    unique_visitors = db.query(func.count(func.distinct(PageView.ip_address))).filter(
        PageView.viewed_at >= since_date
    ).scalar()
    
    # Popular pages
    popular_pages_query = db.query(
        PageView.page,
        func.count(PageView.id).label("views")
    ).filter(
        PageView.viewed_at >= since_date
    ).group_by(PageView.page).order_by(func.count(PageView.id).desc()).limit(10)
    
    popular_pages = {row.page: row.views for row in popular_pages_query}
    
    return AnalyticsStats(
        total_views=total_views or 0,
        unique_visitors=unique_visitors or 0,
        popular_pages=popular_pages
    )
