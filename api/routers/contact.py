"""
Contact router for contact form endpoints.
"""
from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from datetime import datetime, timedelta

from api.database import get_db
from api.models import Contact
from api.schemas import ContactCreate, ContactSchema
from api.services.email_service import send_contact_email

router = APIRouter()

# Simple rate limiting (in production, use Redis or proper rate limiter)
contact_timestamps = {}


@router.post("/contact", response_model=ContactSchema, status_code=201)
async def submit_contact(
    contact_data: ContactCreate,
    request: Request,
    db: Session = Depends(get_db)
):
    """
    Submit contact form and send email.
    
    Args:
        contact_data: Contact form data
        request: FastAPI request object
        
    Returns:
        ContactSchema: Created contact record
    """
    # Get client IP for rate limiting
    client_ip = request.client.host if request.client else "unknown"
    
    # Simple rate limiting: 5 submissions per hour per IP
    now = datetime.utcnow()
    if client_ip in contact_timestamps:
        recent_submissions = [
            ts for ts in contact_timestamps[client_ip]
            if now - ts < timedelta(hours=1)
        ]
        if len(recent_submissions) >= 5:
            raise HTTPException(
                status_code=429,
                detail="Too many submissions. Please try again later."
            )
        contact_timestamps[client_ip] = recent_submissions + [now]
    else:
        contact_timestamps[client_ip] = [now]
    
    # Create contact record
    contact = Contact(
        name=contact_data.name,
        email=contact_data.email,
        subject=contact_data.subject,
        message=contact_data.message,
        ip_address=client_ip,
        user_agent=request.headers.get("user-agent", "")
    )
    
    db.add(contact)
    db.commit()
    db.refresh(contact)
    
    # Send email asynchronously
    try:
        await send_contact_email(
            name=contact_data.name,
            email=contact_data.email,
            subject=contact_data.subject or "No Subject",
            message=contact_data.message
        )
    except Exception as e:
        print(f"Failed to send email: {e}")
        # Don't fail the request if email fails
    
    return contact
