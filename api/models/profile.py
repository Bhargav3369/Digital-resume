"""
Profile database model for user information.
"""
from sqlalchemy import Column, Integer, String, Text
from api.database import Base


class Profile(Base):
    """User profile information."""
    
    __tablename__ = "profiles"
    
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(100), nullable=False)
    title = Column(String(200), nullable=False)
    bio = Column(Text, nullable=False)
    email = Column(String(100), nullable=False)
    linkedin_url = Column(String(255))
    github_url = Column(String(255))
    twitter_url = Column(String(255))
    location = Column(String(100))
    phone = Column(String(20))
    
    def __repr__(self):
        return f"<Profile {self.full_name}>"
