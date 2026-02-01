"""
Analytics database model.
"""
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from api.database import Base


class PageView(Base):
    """Page view analytics."""
    
    __tablename__ = "page_views"
    
    id = Column(Integer, primary_key=True, index=True)
    page = Column(String(100), nullable=False)  # e.g., "/", "/resume", "/projects"
    ip_address = Column(String(45))  # Anonymized for privacy
    user_agent = Column(String(255))
    referrer = Column(String(255))
    viewed_at = Column(DateTime, default=datetime.utcnow, index=True)
    
    def __repr__(self):
        return f"<PageView {self.page} at {self.viewed_at}>"
