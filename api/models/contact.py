"""
Contact form submission database model.
"""
from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from api.database import Base


class Contact(Base):
    """Contact form submissions."""
    
    __tablename__ = "contacts"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    subject = Column(String(200))
    message = Column(Text, nullable=False)
    submitted_at = Column(DateTime, default=datetime.utcnow)
    ip_address = Column(String(45))  # Support IPv6
    user_agent = Column(String(255))
    
    def __repr__(self):
        return f"<Contact from {self.name} ({self.email})>"
