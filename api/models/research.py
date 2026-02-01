"""
Research database model.
"""
from sqlalchemy import Column, Integer, String, Text, Date
from api.database import Base


class Research(Base):
    """Research work and publications."""
    
    __tablename__ = "research"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    start_date = Column(Date)
    end_date = Column(Date, nullable=True)  # NULL if ongoing
    institution = Column(String(200))
    publication_url = Column(String(255))
    status = Column(String(50))  # e.g., "Published", "In Progress", "Completed"
    
    def __repr__(self):
        return f"<Research {self.title}>"
