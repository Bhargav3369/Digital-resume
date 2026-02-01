"""
Education database model.
"""
from sqlalchemy import Column, Integer, String, Text, Date, Float
from api.database import Base


class Education(Base):
    """Education history."""
    
    __tablename__ = "education"
    
    id = Column(Integer, primary_key=True, index=True)
    degree = Column(String(200), nullable=False)
    institution = Column(String(200), nullable=False)
    location = Column(String(100))
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=True)  # NULL if currently studying
    gpa = Column(Float, nullable=True)
    description = Column(Text)
    achievements = Column(Text)  # Comma-separated or JSON
    
    def __repr__(self):
        return f"<Education {self.degree} at {self.institution}>"
