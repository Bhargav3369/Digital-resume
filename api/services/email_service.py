"""
Email service for sending contact form emails.
"""
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

load_dotenv()

SMTP_HOST = os.getenv("SMTP_HOST", "smtp.gmail.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
RECIPIENT_EMAIL = os.getenv("SMTP_USER")  # Send to yourself


async def send_contact_email(name: str, email: str, subject: str, message: str):
    """
    Send contact form email via SMTP.
    
    Args:
        name: Sender's name
        email: Sender's email
        subject: Email subject
        message: Email message
        
    Returns:
        bool: True if email sent successfully
    """
    try:
        # Create message
        msg = MIMEMultipart("alternative")
        msg["Subject"] = f"Contact Form: {subject}"
        msg["From"] = SMTP_USER
        msg["To"] = RECIPIENT_EMAIL
        
        # Email body
        html = f"""
        <html>
            <body style="font-family: Arial, sans-serif; padding: 20px;">
                <h2 style="color: #6366f1;">New Contact Form Submission</h2>
                <div style="background: #f8fafc; padding: 20px; border-radius: 8px; margin: 20px 0;">
                    <p><strong>Name:</strong> {name}</p>
                    <p><strong>Email:</strong> {email}</p>
                    <p><strong>Subject:</strong> {subject}</p>
                </div>
                <div style="background: #ffffff; padding: 20px; border-left: 4px solid #6366f1;">
                    <h3>Message:</h3>
                    <p style="white-space: pre-wrap;">{message}</p>
                </div>
                <hr style="margin: 30px 0; border: none; border-top: 1px solid #e2e8f0;">
                <p style="color: #94a3b8; font-size: 12px;">
                    This email was sent from your digital resume contact form.
                </p>
            </body>
        </html>
        """
        
        # Attach HTML content
        part = MIMEText(html, "html")
        msg.attach(part)
        
        # Send email
        with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USER, SMTP_PASSWORD)
            server.send_message(msg)
        
        return True
        
    except Exception as e:
        print(f"Error sending email: {e}")
        return False
