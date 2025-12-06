# KNU Student Syllabus Portal

A comprehensive web application for Kazi Nazrul University students to access and manage their course syllabus with real-time search, QR code generation, and PDF downloads.

## Project Overview

This is a full-stack application built with:
- **Frontend**: React 18, Vite, Tailwind CSS, Framer Motion
- **Backend**: Python Flask, SQLAlchemy, JWT Authentication

## Features

### Student Features
✅ Secure login and registration
✅ Unique roll number validation
✅ Auto password generation
✅ Student dashboard with real-time search
✅ Course and semester selection
✅ Subject filtering by type
✅ Unit and sub-unit viewing
✅ QR code generation for syllabus
✅ PDF syllabus download
✅ Print functionality
✅ Profile management
✅ Password change and reset
✅ Activity log tracking
✅ Bookmark subjects
✅ Recent subjects tracking

### Admin Features
✅ Admin dashboard with analytics
✅ Course management (CRUD)
✅ Semester management (CRUD)
✅ Subject management (CRUD)
✅ Unit and sub-unit management
✅ Student list management
✅ Activity log viewing
✅ Analytics dashboard
✅ Data backup and restore
✅ Login analytics

### UI/UX Features
✅ Responsive design (mobile, tablet, desktop)
✅ Light and dark theme support
✅ Smooth animations and transitions
✅ Real-time search suggestions
✅ Loading states and error handling
✅ Toast notifications
✅ Professional design with Lucide icons
✅ Animated university logo
✅ Sidebar navigation
✅ Quick access menu
✅ Search filters

## Project Structure

```
KNU SYLLABUS/
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── store/
│   │   ├── utils/
│   │   ├── styles/
│   │   ├── App.jsx
│   │   └── main.jsx
│   ├── public/
│   ├── index.html
│   ├── package.json
│   ├── vite.config.js
│   ├── tailwind.config.js
│   ├── postcss.config.js
│   └── README.md
│
└── backend/
    ├── app/
    │   ├── models/
    │   │   ├── user.py
    │   │   ├── course.py
    │   │   ├── semester.py
    │   │   ├── subject.py
    │   │   ├── unit.py
    │   │   ├── sub_unit.py
    │   │   └── activity_log.py
    │   ├── routes/
    │   │   ├── auth.py
    │   │   ├── courses.py
    │   │   ├── semesters.py
    │   │   ├── subjects.py
    │   │   ├── units.py
    │   │   ├── students.py
    │   │   ├── syllabus.py
    │   │   ├── admin.py
    │   │   └── search.py
    │   ├── utils/
    │   │   ├── validators.py
    │   │   ├── otp.py
    │   │   ├── qr_generator.py
    │   │   └── pdf_generator.py
    │   └── __init__.py
    ├── run.py
    ├── requirements.txt
    ├── .env
    └── README.md
```

## Quick Start

### Backend Setup

1. Navigate to backend directory:
```bash
cd backend
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. Configure environment variables in `.env`

4. Run the server:
```bash
python run.py
```

The backend will run on `http://localhost:5000`

### Frontend Setup

1. Navigate to frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start development server:
```bash
npm run dev
```

The frontend will run on `http://localhost:3000`

## API Endpoints

### Authentication
- `POST /api/auth/register` - Register new student
- `POST /api/auth/login` - Student login
- `POST /api/auth/forgot-password` - Request password reset
- `POST /api/auth/verify-otp` - Verify OTP
- `POST /api/auth/reset-password` - Reset password

### Courses & Subjects
- `GET /api/courses` - Get all courses
- `GET /api/semesters/course/<id>` - Get semesters by course
- `GET /api/subjects/semester/<id>` - Get subjects by semester
- `GET /api/units/subject/<id>` - Get units by subject

### Syllabus
- `GET /api/syllabus/<id>` - Get syllabus
- `GET /api/syllabus/<id>/pdf` - Download PDF
- `GET /api/syllabus/<id>/qr` - Generate QR code

### Search
- `GET /api/search/subjects?q=query` - Search subjects
- `POST /api/search/advanced` - Advanced search

### Admin
- `GET /api/admin/dashboard` - Dashboard stats
- `GET /api/admin/analytics` - Analytics data
- `POST /api/admin/backup` - Backup data

## Database Schema

### Users Table
- id (Primary Key)
- name
- email (Unique)
- password_hash
- phone
- profile_picture
- user_type (student/admin)
- is_active
- created_at
- updated_at

### Students Table
- id (Primary Key)
- user_id (Foreign Key)
- roll_number (Unique)
- father_name
- course_id (Foreign Key)
- semester_id (Foreign Key)
- enrollment_date

### Courses Table
- id (Primary Key)
- name (Unique)
- code (Unique)
- description
- duration_years
- created_at
- updated_at

### Semesters Table
- id (Primary Key)
- course_id (Foreign Key)
- number
- start_date
- end_date
- is_active
- created_at
- updated_at

### Subjects Table
- id (Primary Key)
- course_id (Foreign Key)
- semester_id (Foreign Key)
- name
- code (Unique)
- description
- credits
- subject_type
- created_at
- updated_at

### Units Table
- id (Primary Key)
- subject_id (Foreign Key)
- number
- title
- description
- content
- created_at
- updated_at

### SubUnits Table
- id (Primary Key)
- unit_id (Foreign Key)
- number
- title
- content
- created_at
- updated_at

### ActivityLogs Table
- id (Primary Key)
- user_id (Foreign Key)
- action
- description
- ip_address
- created_at

## Technologies & Dependencies

### Frontend
- React 18.2.0
- Vite 5.0.0
- Tailwind CSS 3.3.0
- Framer Motion 10.16.0
- Axios 1.6.0
- Zustand 4.4.0
- React Router 6.20.0
- Lucide React 0.292.0
- QRCode 1.0.1

### Backend
- Flask 3.0.0
- Flask-SQLAlchemy 3.1.1
- Flask-JWT-Extended 4.5.2
- SQLAlchemy 2.0.23
- bcrypt 4.1.1
- python-dotenv 1.0.0
- qrcode 7.4.2
- Pillow 10.1.0
- PyPDF2 4.0.1

## Security Features

- ✅ Password hashing with bcrypt
- ✅ JWT-based authentication
- ✅ CORS enabled for frontend
- ✅ Role-based access control
- ✅ Input validation and sanitization
- ✅ SQL injection prevention
- ✅ OTP verification for password reset
- ✅ Activity logging
- ✅ Secure token storage

## Performance Optimizations

- Code splitting with Vite
- Lazy loading of routes
- Image optimization
- Minified CSS and JavaScript
- Database query optimization
- Caching strategies
- Fast refresh during development

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## Deployment

### Frontend Deployment
The frontend can be deployed to:
- Netlify
- Vercel
- GitHub Pages
- AWS S3 + CloudFront

### Backend Deployment
The backend can be deployed to:
- Heroku
- AWS EC2
- DigitalOcean
- Google Cloud Platform
- Azure

## Development Guidelines

1. Follow the existing code structure
2. Use meaningful variable and function names
3. Add comments for complex logic
4. Test all features before committing
5. Use Git for version control
6. Keep frontend and backend separate
7. Update documentation when adding features

## Troubleshooting

### Frontend Issues
- Clear node_modules and reinstall: `rm -rf node_modules && npm install`
- Clear cache: `npm cache clean --force`
- Check Vite config for API proxy settings

### Backend Issues
- Ensure Python 3.8+ is installed
- Check database connection in .env
- Verify all dependencies are installed
- Check port 5000 is not in use

## Future Enhancements

- [ ] Mobile app (React Native)
- [ ] Email notifications
- [ ] SMS notifications
- [ ] Video lectures integration
- [ ] Assignment submission system
- [ ] Grading system
- [ ] Discussion forums
- [ ] Real-time notifications
- [ ] Multi-language support
- [ ] Advanced analytics dashboard

## License

© 2024 Kazi Nazrul University. All rights reserved.

## Support

For support and issues, please contact the development team or create an issue in the repository.

## Contributors

- Development Team
- Kazi Nazrul University

---

**Last Updated**: December 2024
