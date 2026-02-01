"""
Skill database model.
"""
from sqlalchemy import Column, Integer, String
from api.database import Base


class Skill(Base):
    """Skills categorized by type."""
    
    __tablename__ = "skills"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    category = Column(String(50), nullable=False)  # e.g., "Languages", "Frameworks", "Tools"
    proficiency = Column(String(20))  # e.g., "Beginner", "Intermediate", "Advanced", "Expert"
    order = Column(Integer, default=0)  # For custom sorting
    
    def __repr__(self):
        return f"<Skill {self.name} ({self.category})>"
