# Bhargav's Digital Resume

A full-stack digital resume built with **FastAPI** and **React**.

## Project Features
- **Modern UI**: Dark mode, glassmorphism, and smooth transitions.
- **Dynamic Content**: Data served via a RESTful API from a PostgreSQL database.
- **Interactive Portfolio**: Research work, education history, and project showcase with filtering.
- **Analytics**: Built-in page view tracking and project engagement stats.
- **Contact System**: Rate-limited contact form with automatic email notifications.

## Tech Stack
- **Frontend**: React 18, Vite, Framer Motion, Lucide Icons.
- **Backend**: FastAPI, SQLAlchemy ORM, Mangum (Vercel Adapter).
- **Database**: PostgreSQL (Production-ready).

---

## Local Development Setup

### 1. Prerequisites
- Python 3.9+
- Node.js & npm

### 2. Backend Setup
```bash
cd api
pip install -r requirements.txt

# Initializing the database (SQLite for local, PostgreSQL for production)
# Make sure to set DATABASE_URL in a .env file
python -m api.utils.init_db
```

### 3. Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

### 4. Running the full stack locally
You can use the Vercel CLI to run both frontend and backend concurrently:
```bash
vercel dev
```

---

## Deployment to Vercel

### 1. Database Setup
1. Create a free PostgreSQL database on [Neon](https://neon.tech/) or [Supabase](https://supabase.com/).
2. Get your `DATABASE_URL`.

### 2. Configure Vercel
1. Install Vercel CLI: `npm install -g vercel`.
2. Run `vercel` in the root directory.
3. In the Vercel Dashboard, add the following Environment Variables:
   - `DATABASE_URL`: Your PostgreSQL connection string.
   - `SMTP_HOST`: e.g., `smtp.gmail.com`
   - `SMTP_PORT`: `587`
   - `SMTP_USER`: Your email address.
   - `SMTP_PASSWORD`: Your app-specific password.

### 3. Deploy
```bash
vercel --prod
```

## Testing the API
Once the backend is running, you can access the interactive Swagger documentation at:
- **Local**: `http://localhost:8000/docs`
- **Production**: `https://your-deployment-url.vercel.app/docs`

---

## Verification
I've included a script `api/verify_backend.py` to check basic connectivity of the backend endpoints.
To run it:
```bash
python api/verify_backend.py
```
