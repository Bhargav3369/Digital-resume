# Digital Resume Application - Implementation Plan

A modern, interactive digital resume built with React + Vite frontend and FastAPI backend. The application will showcase professional experience, projects, skills, and provide a contact mechanism.

## User Requirements - Finalized ✅

**Resume Sections**:
- About Me
- Research Work
- Education
- Skills
- Projects

**Architecture**:
- **Data Strategy**: Full-stack - FastAPI + Python backend serving all resume data via RESTful API
- **Database**: PostgreSQL (Neon/Supabase/Vercel Postgres) for content and analytics
- **Navigation**: Multi-route with React Router (separate pages at `/`, `/resume`, `/projects`, `/contact`)
- **Deployment**: **Vercel for both frontend and backend** (serverless functions)

**Features**:
- ✅ Dark mode design
- ✅ Downloadable PDF resume
- ✅ Contact form with email functionality
- ✅ Project cards with: title, description, tech stack, GitHub link

**Technology Stack**:
- **Frontend**: React 18 + Vite, React Router, Axios for API calls
- **Backend**: FastAPI, Mangum (serverless adapter), SQLAlchemy ORM, Pydantic validation, Python-SMTP
- **Database**: PostgreSQL (Neon/Supabase/Vercel Postgres - free tier available)
- **Deployment**: Vercel (frontend + backend serverless functions)

## Proposed Changes

### Frontend Architecture

The application will be built using React 18 + Vite with a component-based architecture following the structure you provided.

#### Technology Stack
- **Framework**: React 18.x
- **Build Tool**: Vite (latest)
- **Routing**: React Router v6
- **HTTP Client**: Axios
- **Styling**: CSS3 (with CSS variables for theming)
- **Icons**: React Icons or Lucide React
- **Animations**: Framer Motion (optional for smooth transitions)

---

### Project Structure (Vercel Monorepo)

```
resume-app/
├── frontend/
│   ├── public/
│   │   ├── assets/              # Images, icons
│   │   └── resume.pdf           # Downloadable resume PDF
│   ├── src/
│   │   ├── components/
│   │   │   ├── Navbar.jsx       # Multi-route navigation
│   │   │   ├── ResumeCard.jsx   # Display resume sections
│   │   │   ├── ProjectCard.jsx  # Individual project showcase
│   │   │   ├── SkillBadge.jsx   # Skill tags/badges
│   │   │   └── Footer.jsx       # Footer component
│   │   │
│   │   ├── pages/
│   │   │   ├── Home.jsx         # Landing page with About Me
│   │   │   ├── Resume.jsx       # Research, Education, Skills
│   │   │   ├── Projects.jsx     # Projects showcase
│   │   │   └── Contact.jsx      # Contact form
│   │   │
│   │   ├── services/
│   │   │   └── api.js           # Axios instance & API endpoints
│   │   │
│   │   ├── styles/
│   │   │   ├── index.css        # Global styles, dark theme
│   │   │   └── variables.css    # CSS custom properties
│   │   │
│   │   ├── App.jsx              # React Router setup
│   │   └── main.jsx             # Entry point
│   │
│   ├── index.html
│   ├── vite.config.js
│   └── package.json
│
├── api/                         # Vercel Serverless Functions
│   ├── index.py                 # Main FastAPI app with mangum
│   ├── database.py              # PostgreSQL connection
│   ├── dependencies.py
│   │
│   ├── models/                  # SQLAlchemy models
│   │   ├── profile.py
│   │   ├── research.py
│   │   ├── education.py
│   │   ├── skill.py
│   │   ├── project.py
│   │   ├── contact.py
│   │   └── analytics.py
│   │
│   ├── schemas/                 # Pydantic schemas
│   │   └── ...
│   │
│   ├── routers/                 # API routes
│   │   ├── profile.py
│   │   ├── skills.py
│   │   ├── projects.py
│   │   ├── contact.py
│   │   └── analytics.py
│   │
│   ├── services/
│   │   └── email_service.py
│   │
│   └── requirements.txt         # Python dependencies
│
├── vercel.json                  # Vercel configuration
├── .env.example
└── README.md
```

---

### Vercel Configuration

#### [NEW] [vercel.json](file:///c:/Users/DELL/Documents/coding/Sem-7/Resume/vercel.json)

**Purpose**: Configure Vercel to serve frontend and route API requests to FastAPI serverless functions

```json
{
  "buildCommand": "cd frontend && npm run build",
  "outputDirectory": "frontend/dist",
  "devCommand": "cd frontend && npm run dev",
  "installCommand": "cd frontend && npm install && cd ../api && pip install -r requirements.txt",
  "functions": {
    "api/index.py": {
      "runtime": "python3.9",
      "maxDuration": 10
    }
  },
  "rewrites": [
    {
      "source": "/api/:path*",
      "destination": "/api/index.py"
    }
  ]
}
```

**Configuration Explained**:
- `buildCommand`: Build the Vite React app from frontend directory
- `outputDirectory`: Output directory for built frontend assets
- `functions`: Define Python serverless function with 10s timeout
- `rewrites`: Route all `/api/*` requests to FastAPI serverless handler
- During deployment, Vercel automatically detects and serves the frontend while routing API calls to the Python function

---

### Component Design

#### [NEW] [Navbar.jsx](file:///c:/Users/DELL/Documents/coding/Sem-7/Resume/frontend/src/components/Navbar.jsx)

**Purpose**: Top navigation bar with links to different sections/pages

**Features**:
- Responsive design (hamburger menu for mobile)
- Active link highlighting
- Smooth scroll behavior or React Router navigation
- Fixed/sticky positioning option

**Props**: None (self-contained)

#### [NEW] [ResumeCard.jsx](file:///c:/Users/DELL/Documents/coding/Sem-7/Resume/frontend/src/components/ResumeCard.jsx)

**Purpose**: Reusable card component for resume sections

**Features**:
- Display section title, content, dates, descriptions
- Support for various content types (work experience, education, certifications)
- Icons for different section types

**Props**:
```javascript
{
  title: string,
  subtitle: string,
  date: string,
  description: string,
  skills: array,
  icon: component
}
```

#### [NEW] [ProjectCard.jsx](file:///c:/Users/DELL/Documents/coding/Sem-7/Resume/frontend/src/components/ProjectCard.jsx)

**Purpose**: Showcase individual projects

**Features**:
- Project thumbnail/image
- Title, description, tech stack
- Links to live demo and GitHub repository
- Hover effects with additional details

**Props**:
```javascript
{
  title: string,
  description: string,
  techStack: array,      // Array of technologies used
  githubUrl: string      // GitHub repository link
}
```

#### [NEW] [SkillBadge.jsx](file:///c:/Users/DELL/Documents/coding/Sem-7/Resume/frontend/src/components/SkillBadge.jsx)

**Purpose**: Display individual skills as styled badges

**Features**:
- Category-based color coding
- Proficiency level indicator (optional)
- Hover effects

**Props**:
```javascript
{
  name: string,
  category: string,
  level: string
}
```

---

### Page Design

#### [NEW] [Home.jsx](file:///c:/Users/DELL/Documents/coding/Sem-7/Resume/frontend/src/pages/Home.jsx)

**Purpose**: Landing page with hero section and About Me

**Content**:
- Hero section with name, title, tagline
- **About Me** section with bio and introduction
- Professional photo/avatar
- Call-to-action buttons (View Resume, View Projects, Contact)
- Quick links to social profiles (GitHub, LinkedIn, etc.)

#### [NEW] [Resume.jsx](file:///c:/Users/DELL/Documents/coding/Sem-7/Resume/frontend/src/pages/Resume.jsx)

**Purpose**: Comprehensive resume view

**Sections**:
- Research Work (using ResumeCard)
- Education (using ResumeCard)
- Skills (using SkillBadge, categorized by type)
- Download Resume button (PDF - links to `/public/resume.pdf`)

#### [NEW] [Projects.jsx](file:///c:/Users/DELL/Documents/coding/Sem-7/Resume/frontend/src/pages/Projects.jsx)

**Purpose**: Portfolio/projects showcase

**Features**:
- Grid layout of ProjectCard components
- Filter by technology/category
- Sort by date/featured
- Pagination or infinite scroll

#### [NEW] [Contact.jsx](file:///c:/Users/DELL/Documents/coding/Sem-7/Resume/frontend/src/pages/Contact.jsx)

**Purpose**: Contact form and information

**Features**:
- Contact form (name, email, subject, message)
- Form validation (email format, required fields)
- Integration with **EmailJS** for serverless email sending (no backend needed)
- Email/social links from profile data
- Success/error feedback messages
- Loading state during submission

---

### API Integration Layer

#### [NEW] [api.js](file:///c:/Users/DELL/Documents/coding/Sem-7/Resume/frontend/src/services/api.js)

**Purpose**: Centralized API communication with FastAPI backend

**Axios Configuration**:
```javascript
import axios from 'axios';

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: { 'Content-Type': 'application/json' }
});

// API endpoints
export const profileAPI = {
  getProfile: () => api.get('/api/profile'),
  getResearch: () => api.get('/api/research'),
  getEducation: () => api.get('/api/education'),
  getSkills: () => api.get('/api/skills'),
};

export const projectsAPI = {
  getAllProjects: () => api.get('/api/projects'),
  getProjectById: (id) => api.get(`/api/projects/${id}`),
};

export const contactAPI = {
  sendMessage: (data) => api.post('/api/contact', data),
};

export const analyticsAPI = {
  trackPageView: (page) => api.post('/api/analytics/pageview', { page }),
};
```

**Features**:
- Environment-based API URL configuration
- Error handling with interceptors
- Loading states support
- Request/response transformation

---

### Styling Approach

#### [NEW] [index.css](file:///c:/Users/DELL/Documents/coding/Sem-7/Resume/frontend/src/styles/index.css) + [variables.css](file:///c:/Users/DELL/Documents/coding/Sem-7/Resume/frontend/src/styles/variables.css)

**Dark Mode Design System**:
- CSS custom properties for dark theme
- Background: Deep dark (#0a0a0f, #1a1a2e)
- Accent colors: Vibrant gradients (purple/blue/cyan)
- Text: High contrast whites and light grays
- Responsive typography scale (clamp for fluid sizing)
- Spacing scale (consistent margins/padding)
- Reusable utility classes

**Premium Dark Mode Elements**:
- Smooth color gradients for accents
- Glassmorphism effects (backdrop-blur with transparency)
- Glow effects on hover (box-shadow with accent colors)
- Subtle animations and transitions (0.3s ease)
- Card shadows with colored borders
- Polished, modern aesthetic

---

### FastAPI Backend Architecture (Vercel Serverless)

**Full-stack Python backend** deployed as Vercel serverless functions using **Mangum** adapter.

```
api/
├── index.py                 # FastAPI app with Mangum handler (entry point)
├── database.py              # PostgreSQL connection with SQLAlchemy
├── dependencies.py          # Shared dependencies
│
├── models/                  # SQLAlchemy ORM models
│   ├── __init__.py
│   ├── profile.py           # Profile, About Me
│   ├── research.py          # Research publications
│   ├── education.py         # Education records
│   ├── skill.py             # Skills
│   ├── project.py           # Projects
│   ├── contact.py           # Contact form submissions
│   └── analytics.py         # Page views, visitor stats
│
├── schemas/                 # Pydantic schemas for validation
│   ├── __init__.py
│   ├── profile.py
│   ├── research.py
│   ├── education.py
│   ├── skill.py
│   ├── project.py
│   ├── contact.py
│   └── analytics.py
│
├── routers/                 # API endpoints
│   ├── __init__.py
│   ├── profile.py           # GET /api/profile, /api/research, /api/education
│   ├── skills.py            # GET /api/skills
│   ├── projects.py          # GET /api/projects, GET /api/projects/{id}
│   ├── contact.py           # POST /api/contact (send email)
│   └── analytics.py         # POST /api/analytics/pageview, GET /api/analytics/stats
│
├── services/                # Business logic
│   ├── __init__.py
│   └── email_service.py     # SMTP email sending
│
├── utils/
│   ├── __init__.py
│   └── init_db.py           # Database initialization script
│
└── requirements.txt         # Python dependencies
```

#### [NEW] [index.py](file:///c:/Users/DELL/Documents/coding/Sem-7/Resume/api/index.py) - Serverless Entry Point

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum
from routers import profile, skills, projects, contact, analytics

app = FastAPI(title="Digital Resume API")

# CORS for Vercel frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure for production
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(profile.router, prefix="/api")
app.include_router(skills.router, prefix="/api")
app.include_router(projects.router, prefix="/api")
app.include_router(contact.router, prefix="/api")
app.include_router(analytics.router, prefix="/api")

# Mangum handler for Vercel
handler = Mangum(app)
```

#### Key Backend Features

**1. Resume Content API**
- Serve all resume data from PostgreSQL database
- CRUD operations for managing content
- Structured data with proper relationships
- **Database Options**: Neon (recommended), Supabase, Vercel Postgres - all have free tiers

**2. Contact Form with Email**
- Accept contact form submissions
- Send emails via SMTP (Gmail, SendGrid, etc.)
- Store submissions in database for tracking
- Rate limiting to prevent spam (serverless-friendly)

**3. Analytics & Tracking**
- Track page views and visitor statistics
- Popular projects/sections analytics
- Unique visitors tracking (IP-based with anonymization)
- Time-series data for insights

**4. Projects Management**
- Full CRUD for projects
- Filter by technology, category
- Featured projects flag
- View count tracking per project

**Vercel Serverless Considerations**:
- Connection pooling handled by database provider (Neon, Supabase)
- Cold starts: First request ~1-2s, subsequent requests fast
- PostgreSQL required (SQLite not compatible with serverless)

---

## Implementation Phases

### Phase 1: Backend Foundation
1. Initialize FastAPI project in `/api` folder (Vercel structure)
2. Set up virtual environment and dependencies (`fastapi`, `mangum`, `sqlalchemy`, `psycopg2-binary`)
3. Set up PostgreSQL database (create free Neon/Supabase account)
4. Configure SQLAlchemy with PostgreSQL connection
5. Create database models (Profile, Research, Education, Skill, Project, Contact, Analytics)
6. Create Pydantic schemas for validation
7. Set up database initialization script with sample data
8. Create `index.py` with Mangum handler

### Phase 2: Backend API Development
1. **Profile Router**: GET endpoints for profile, research, education
2. **Skills Router**: GET endpoint for categorized skills
3. **Projects Router**: GET all projects, GET project by ID
4. **Contact Router**: POST endpoint with email service integration
5. **Analytics Router**: POST pageview tracking, GET stats
6. Configure CORS for frontend communication
7. Test locally with `vercel dev`
8. Test all endpoints with Swagger/ReDoc

### Phase 3: Frontend Setup
1. Initialize Vite + React project in `/frontend`
2. Install dependencies: `react-router-dom`, `axios`, `react-icons`, `framer-motion`
3. Set up folder structure (components, pages, services, styles)
4. Create dark mode design system in `variables.css` and `index.css`
5. Set up React Router in `App.jsx`
6. Create Axios API service layer

### Phase 4: Core Components
1. Build `Navbar.jsx` with React Router links
2. Create `SkillBadge.jsx` with category colors
3. Build `ResumeCard.jsx` for research/education
4. Build `ProjectCard.jsx` with GitHub links
5. Create `Footer.jsx`
6. Add loading states and error handling components

### Phase 5: Pages Development with API Integration
1. **Home.jsx**: Hero + About Me (fetch from API)
2. **Resume.jsx**: Research, Education, Skills (fetch from API) + PDF download
3. **Projects.jsx**: Project grid with filtering (fetch from API)
4. **Contact.jsx**: Form with backend API submission
5. Implement page view analytics tracking

### Phase 6: Styling & Polish
1. Implement dark mode color scheme
2. Add glassmorphism effects
3. Create smooth transitions and animations
4. Add hover effects and micro-interactions
5. Ensure responsive design (mobile, tablet, desktop)
6. Loading skeletons for API data

### Phase 7: Integration Testing
1. Test frontend-backend communication
2. Verify all API endpoints work correctly
3. Test contact form email delivery
4. Add PDF resume to `/public/resume.pdf`
5. Test error handling and edge cases
6. Performance optimization
7. Cross-browser testing

### Phase 8: Deployment to Vercel
1. Create `vercel.json` configuration file
2. Set up PostgreSQL database (Neon/Supabase/Vercel Postgres)
3. Configure environment variables in Vercel dashboard:
   - `DATABASE_URL` (PostgreSQL connection string)
   - `SMTP_HOST`, `SMTP_PORT`, `SMTP_USER`, `SMTP_PASSWORD`
4. Deploy to Vercel: `vercel --prod`
5. Run database migrations/seed script on production DB
6. Test deployed version end-to-end
7. Set up custom domain (optional)

---

## Dark Mode Design Specifications

### Color Palette
1. **Backgrounds**:
   - Primary: `#0a0a0f` (deep dark)
   - Secondary: `#1a1a2e` (card backgrounds)
   - Accent backgrounds: `#16213e`

2. **Accent Colors**:
   - Primary gradient: `#6366f1 → #8b5cf6` (indigo to purple)
   - Secondary gradient: `#06b6d4 → #3b82f6` (cyan to blue)
   - Success: `#10b981` (emerald)

3. **Text**:
   - Primary: `#f8fafc` (almost white)
   - Secondary: `#cbd5e1` (light gray)
   - Muted: `#94a3b8` (gray)

### Typography
- **Font**: Inter from Google Fonts
- **Headings**: 700 weight, gradient text effects
- **Body**: 400 weight, high contrast

### Visual Elements
1. **Cards**: Dark background with colored border + glow effect on hover
2. **Glassmorphism**: `backdrop-blur(10px)` with `rgba(255,255,255,0.05)` overlay
3. **Shadows**: Colored box-shadows (`0 0 20px rgba(99, 102, 241, 0.5)`)
4. **Buttons**: Gradient backgrounds with hover glow
5. **Transitions**: All animations `0.3s cubic-bezier(0.4, 0, 0.2, 1)`

---

## Verification Plan

### Automated Tests
```bash
# Frontend development server
npm run dev

# Build production bundle
npm run build

# Backend server
uvicorn app.main:app --reload
```

### Manual Verification
1. **Responsive Design**: Test on mobile, tablet, desktop viewports
2. **Navigation**: Verify all routes work correctly
3. **API Integration**: Confirm data loads from backend
4. **Contact Form**: Test form submission and validation
5. **Performance**: Check Lighthouse scores
6. **Cross-browser**: Test on Chrome, Firefox, Safari

### Browser Testing
- Use browser automation to verify navigation flows
- Test form submission
- Verify responsive breakpoints
