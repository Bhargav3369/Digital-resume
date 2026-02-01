"""
Project database model.
"""
from sqlalchemy import Column, Integer, String, Text, Date, Boolean
from api.database import Base


class Project(Base):
    """Portfolio projects."""
    
    __tablename__ = "projects"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=False)
    tech_stack = Column(Text, nullable=False)  # Comma-separated technologies
    github_url = Column(String(255))
    live_url = Column(String(255), nullable=True)
    image_url = Column(String(255), nullable=True)
    start_date = Column(Date)
    end_date = Column(Date, nullable=True)
    featured = Column(Boolean, default=False)
    view_count = Column(Integer, default=0)
    
    def __repr__(self):
        return f"<Project {self.title}>"
