# Bhargav's Digital Resume

A modern, high-performance full-stack digital resume built with **FastAPI** and **React**.

🔗 **Live Demo**: [digital-resume-woad.vercel.app](https://digital-resume-woad.vercel.app/)

## ✨ Key Features
- **Premium UI**: Sleek dark-mode design with glassmorphism and smooth Framer Motion animations.
- **Dynamic Projects**: Automated project grid with real-time filtering and detail views.
- **Deep Research Integration**: Dedicated sections for research publications and academic achievements.
- **Analytics Ready**: Integrated page-view tracking and interaction analytics.
- **Automated Contact**: Secured contact system with backend validation and email delivery.

## 🛠️ Technical Architecture
This project uses a modern monorepo structure designed for Vercel Serverless deployment.

- **Frontend**: React 18 + Vite (Ultra-fast build & HMR)
- **Backend**: FastAPI (Python 3.12) - High-performance asynchronous API
- **Database**: PostgreSQL (Neon) with SQLAlchemy 2.0 ORM
- **Deployment**: Vercel Native Python Integration

For a deep dive into the architecture, see the [Tech Stack Documentation](./TECH_STACK.md).

## 🚀 Quick Start (Local)

1. **Clone & Install**:
   ```bash
   # Install API dependencies
   pip install -r api/requirements.txt
   
   # Install Frontend dependencies
   cd frontend && npm install
   ```

2. **Database Setup**:
   - Create a `.env` file in the root using the provided template.
   - Run the initialization script: `python -m api.utils.init_db`

3. **Run**:
   - Backend: `uvicorn api.index:app --port 8000`
   - Frontend: `cd frontend && npm run dev`

---
*Created by Madala Venkata Bhargav*
