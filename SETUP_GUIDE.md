# KNU Student Syllabus Portal - Complete Setup Guide

## Project Overview

This is a full-stack web application for Kazi Nazrul University students to manage their course syllabus with real-time search, QR code generation, and PDF downloads.

**Technology Stack:**
- Frontend: React 18, Vite, Tailwind CSS, Framer Motion
- Backend: Python Flask, SQLAlchemy, JWT Authentication
- Database: SQLite (development)

## Project Structure

```
KNU SYLLABUS/
├── frontend/                 # React frontend application
│   ├── src/
│   │   ├── components/      # Reusable React components
│   │   ├── pages/           # Page components
│   │   ├── store/           # Zustand state management
│   │   ├── utils/           # Utility functions and API calls
│   │   ├── styles/          # Global CSS styles
│   │   ├── App.jsx
│   │   └── main.jsx
│   ├── package.json
│   ├── vite.config.js
│   ├── tailwind.config.js
│   └── README.md
│
├── backend/                  # Python Flask backend
│   ├── app/
│   │   ├── models/          # Database models
│   │   ├── routes/          # API endpoints
│   │   ├── utils/           # Utility functions
│   │   └── __init__.py      # Flask app factory
│   ├── run.py               # Entry point
│   ├── requirements.txt     # Python dependencies
│   ├── .env                 # Environment variables
│   └── README.md
│
└── README.md                # Main project documentation
```

## Prerequisites

Before you begin, ensure you have installed:

1. **Node.js** (v18 or higher)
   - Download from: https://nodejs.org/
   - Verify: `node -v` and `npm -v`

2. **Python** (v3.8 or higher)
   - Download from: https://www.python.org/
   - Verify: `python --version`

3. **Git** (optional, for version control)
   - Download from: https://git-scm.com/

## Backend Setup

### Step 1: Navigate to Backend Directory

```bash
cd backend
```

### Step 2: Create Virtual Environment (Optional but Recommended)

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Python Dependencies

```bash
pip install --only-binary :all: -r requirements.txt
```

### Step 4: Configure Environment Variables

Edit `.env` file:

```env
FLASK_ENV=development
DEBUG=True
DATABASE_URL=sqlite:///knu_syllabus.db
JWT_SECRET_KEY=your-secret-key-change-in-production
PORT=5000
```

### Step 5: Initialize Database

```bash
python
>>> from app import create_app, db
>>> app = create_app()
>>> with app.app_context():
>>>     db.create_all()
>>> exit()
```

### Step 6: Run Backend Server

```bash
python run.py
```

The backend will start on `http://localhost:5000`

You should see:
```
 * Running on http://127.0.0.1:5000
```

## Frontend Setup

### Step 1: Navigate to Frontend Directory

```bash
cd frontend
```

### Step 2: Install Node Dependencies

```bash
npm install --legacy-peer-deps
```

### Step 3: Configure API Endpoint (Optional)

Edit `src/utils/api.js`:

```javascript
const API_BASE_URL = 'http://localhost:5000/api'
```

### Step 4: Run Development Server

```bash
npm run dev
```

The frontend will start on `http://localhost:3000`

You should see:
```
➜  Local:   http://localhost:3000/
```

## Accessing the Application

1. Open your browser and go to: `http://localhost:3000`
2. You should see the KNU Student Syllabus Portal login page

## Default Credentials (For Testing)

Since this is a new installation, you need to create an account:

1. Click "Create Account" on the login page
2. Fill in the registration form with:
   - Full Name: Your Name
   - Father's Name: Father's Name
   - Phone: Your Phone Number
   - Roll Number: Any unique number (e.g., 2024001)
   - Course: Select a course
   - Semester: Select a semester
   - Email: your.email@example.com
   - Password: Create a password

3. Click "Create Account"
4. You'll be redirected to login
5. Use your email and password to login

## Features Available

### Student Features
✅ Secure login and registration
✅ Real-time syllabus search
✅ Course and semester selection
✅ Subject filtering
✅ Unit and sub-unit viewing
✅ QR code generation
✅ PDF download
✅ Profile management
✅ Password reset with OTP

### Admin Features
✅ Admin dashboard
✅ Course management
✅ Subject management
✅ Student analytics
✅ Activity logging

## API Endpoints

### Authentication
```
POST   /api/auth/register           - Register new student
POST   /api/auth/login              - Student login
GET    /api/auth/check-roll/<roll>  - Check roll number
POST   /api/auth/forgot-password    - Request password reset
POST   /api/auth/verify-otp         - Verify OTP
POST   /api/auth/reset-password     - Reset password
```

### Courses & Subjects
```
GET    /api/courses                 - Get all courses
GET    /api/semesters               - Get all semesters
GET    /api/subjects                - Get all subjects
GET    /api/units/subject/<id>      - Get units by subject
```

### Syllabus
```
GET    /api/syllabus/<id>           - Get syllabus
GET    /api/syllabus/<id>/pdf       - Download PDF
GET    /api/syllabus/<id>/qr        - Generate QR code
```

### Search
```
GET    /api/search/subjects?q=query - Search subjects
POST   /api/search/advanced         - Advanced search
```

## Troubleshooting

### Backend Issues

**Error: "Port 5000 already in use"**
- Solution: Change PORT in `.env` or kill the process using port 5000

**Error: "Database locked"**
- Solution: Delete `knu_syllabus.db` and reinitialize

**Error: "Module not found"**
- Solution: Reinstall dependencies: `pip install --only-binary :all: -r requirements.txt`

### Frontend Issues

**Error: "Cannot find module"**
- Solution: Clear node_modules and reinstall: `rm -rf node_modules && npm install --legacy-peer-deps`

**Error: "API connection refused"**
- Solution: Ensure backend is running on port 5000

**Port 3000 already in use**
- Solution: Change port in `vite.config.js` or kill the process

## Development Workflow

### Making Changes

1. **Frontend Changes:**
   - Edit files in `frontend/src/`
   - Changes auto-reload in browser (Hot Module Replacement)

2. **Backend Changes:**
   - Edit files in `backend/app/`
   - Server auto-reloads (debug mode enabled)

### Adding New Features

1. **Database Model:**
   - Create model in `backend/app/models/`
   - Update `backend/app/models/__init__.py`

2. **API Endpoint:**
   - Create route in `backend/app/routes/`
   - Register in `backend/app/__init__.py`

3. **Frontend Component:**
   - Create component in `frontend/src/components/`
   - Import and use in pages

## Building for Production

### Frontend Build

```bash
cd frontend
npm run build
```

Output will be in `frontend/dist/`

### Backend Deployment

1. Update `.env`:
   ```env
   FLASK_ENV=production
   DEBUG=False
   ```

2. Use production WSGI server (Gunicorn):
   ```bash
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:5000 run:app
   ```

## Database Models

### User
- id, name, email, password_hash, phone, profile_picture, user_type, is_active

### Student
- id, user_id, roll_number, father_name, course_id, semester_id, enrollment_date

### Course
- id, name, code, description, duration_years

### Semester
- id, course_id, number, start_date, end_date, is_active

### Subject
- id, course_id, semester_id, name, code, description, credits, subject_type

### Unit
- id, subject_id, number, title, description, content

### SubUnit
- id, unit_id, number, title, content

### ActivityLog
- id, user_id, action, description, ip_address, created_at

## Security Notes

⚠️ **Important for Production:**

1. Change `JWT_SECRET_KEY` in `.env`
2. Set `DEBUG=False` in `.env`
3. Use HTTPS instead of HTTP
4. Use a production database (PostgreSQL, MySQL)
5. Use a production WSGI server (Gunicorn, uWSGI)
6. Add rate limiting
7. Enable CORS properly
8. Use environment variables for sensitive data

## Performance Tips

1. **Frontend:**
   - Enable code splitting
   - Use lazy loading for routes
   - Optimize images
   - Use CDN for static assets

2. **Backend:**
   - Add database indexes
   - Use caching (Redis)
   - Optimize queries
   - Use connection pooling

## Useful Commands

### Backend
```bash
# Run server
python run.py

# Run in production
gunicorn -w 4 run:app

# Database shell
python
>>> from app import create_app, db
>>> app = create_app()
```

### Frontend
```bash
# Development
npm run dev

# Build
npm run build

# Preview build
npm run preview

# Lint
npm run lint
```

## Support & Documentation

- Frontend README: `frontend/README.md`
- Backend README: `backend/README.md`
- Main README: `README.md`

## Next Steps

1. ✅ Setup complete!
2. 📝 Create test data (courses, subjects, units)
3. 🧪 Test all features
4. 🚀 Deploy to production
5. 📊 Monitor and optimize

## License

© 2024 Kazi Nazrul University. All rights reserved.

---

**Last Updated**: December 2024
**Version**: 1.0.0
