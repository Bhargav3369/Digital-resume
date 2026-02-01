# Tech Stack Overview

This project is a high-performance, modern full-stack digital resume application deployed on Vercel.

## 🚀 The Core Technologies

### 1. Frontend: React + Vite
- **Location**: `/frontend/`
- **Purpose**: Provides a fast, interactive, and responsive user interface.
- **Key Features**: Vite for ultra-fast development/builds, Framer Motion for animations, and Lucide-React for icons.
- **Styling**: Vanilla CSS with a custom dark-mode design system.

### 2. Backend: FastAPI + Python 3.12
- **Location**: `/api/`
- **Purpose**: Handles all data processing, database communication, and analytic services.
- **Key Features**: High-performance asynchronous execution, automatic Swagger documentation, and Mangum-less Vercel integration.

### 3. Database: PostgreSQL (Neon)
- **Engine**: SQLAlchemy 2.0 ORM.
- **Connection**: Managed via Neon's serverless connection pooler for stability.
- **Seeding**: Custom initialization scripts to sync local data with production.

### 4. Deployment: Vercel Monorepo
- **Configuration**: `vercel.json` manages the unified build process.
- **Backend**: Python Serverless Functions.
- **Frontend**: Static site generation for global performance.

## 📁 Project Structure
- `/api`: Python source code, database models, and API routers.
- `/frontend`: React components, service layer, and CSS styles.
- `/frontend/public`: Static assets (Resume PDF, Research Reports).
