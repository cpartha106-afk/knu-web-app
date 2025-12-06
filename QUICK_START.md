# KNU Student Syllabus Portal - Quick Start Guide

## 🚀 Start Using in 2 Minutes

### Backend is Running ✅
- **URL**: http://localhost:5000
- **Status**: Flask development server active

### Frontend is Running ✅
- **URL**: http://localhost:3000
- **Status**: Vite development server active

---

## 📱 Access the Application

### 1. Open Home Page
```
http://localhost:3000/
```
You'll see:
- Animated KNU Logo (rotating with glow effect)
- Welcome message
- Feature showcase
- Statistics (90+ Courses, 358 Semesters, 1790 Subjects, 8950+ Units)

### 2. Create an Account
Click "Sign Up" and fill in:
- Full Name
- Father's Name
- Phone Number
- Roll Number (unique)
- **Course** - Select from 90 available courses
- **Semester** - Auto-populated based on course
- Email
- Password

### 3. Login
Use your email and password to login

### 4. Access Dashboard
After login, you'll see:
- Animated KNU Logo in header
- Sidebar with navigation
- Search panel with course dropdown

### 5. Search Syllabus
1. Select a **Course** from dropdown (90 options)
2. Select a **Semester** (auto-loaded)
3. View all **Subjects** for that semester
4. Click a subject to view full syllabus
5. Download PDF or generate QR code

---

## 🎨 Logo Features

The animated KNU logo appears in:
- ✅ Home page (large, hero section)
- ✅ Login page (large, header)
- ✅ Registration page (large, header)
- ✅ Dashboard (medium, header)
- ✅ Sidebar (medium, navigation)

**Logo Animations:**
- Smooth rotation
- Scaling effects
- Glowing aura
- Gradient colors (Blue → Purple → Pink)

---

## 📚 Available Courses (90 Total)

### Bachelor Programs (15)
BCA, BCS, B.Sc IT, BSE, BDS, BCE, BAI, BCS Cyber, BCC, BWT, BMA, BNT, BMAA, BGD, BCG

### Master Programs (10)
MCA, MCS, M.Sc IT, MSE, MDS, MAI, MML, MCC, MCSec, MCN

### Diploma Programs (25)
DCA, DIT, DSE, DCE, DHN, DCP, DWD, DAD, DGD, DAVFX, DCS, DCC, DDS, DML, DAI, DDBM, DCN, DCG, DFSD, DUX, DIS, DCH, DOA, DCSec, DEH

### Certificate Programs (30)
CCB, CMSO, CAE, CWD, CFD, CBD, CFSD, CPP, CJP, CCP, CCPP, CSD, CDA, CAI, CML, CCS, CEH, CCC, CN, CCT, CTG, CDM, CST, CMR, CA, CVE, CGD, CDE, CCA, CCSec

### Advanced Diploma Programs (10)
ADCA, ADIT, ADSE, ADWE, ADAIML, ADCS, ADCC, ADDA, ADN, ADDF

---

## 📊 Syllabus Structure

Each course has:
- **Semesters**: Based on course duration (2-4 years)
- **Subjects**: 5 per semester
  - Major Theory
  - Minor Theory
  - Supporting Theory
  - Major Practical
  - Minor Practical
- **Units**: 5 per subject
- **Sub-Units**: 3 per unit

**Example Path:**
```
BCA (3-year program)
├── Semester 1
│   ├── Subject 1 (Major Theory)
│   │   ├── Unit 1
│   │   │   ├── Sub-Unit 1.1
│   │   │   ├── Sub-Unit 1.2
│   │   │   └── Sub-Unit 1.3
│   │   ├── Unit 2
│   │   └── ...
│   ├── Subject 2 (Minor Theory)
│   └── ...
├── Semester 2
└── ...
```

---

## 🔐 Test Credentials

**Create your own account:**
1. Go to http://localhost:3000/register
2. Fill in the form
3. Select any course
4. Create account
5. Login

**Or use the API directly:**
```bash
# Register
curl -X POST http://localhost:5000/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Test Student",
    "fatherName": "Father Name",
    "email": "test@example.com",
    "phone": "1234567890",
    "rollNumber": "2024001",
    "courseId": 1,
    "semesterId": 1,
    "password": "password123"
  }'

# Login
curl -X POST http://localhost:5000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "password": "password123"
  }'
```

---

## 🎯 Key Features

### ✅ Animated Logo
- Professional design with gradients
- Smooth animations
- Responsive sizing
- Used throughout app

### ✅ 90 Courses
- All programs listed
- Professional descriptions
- Unique course codes
- Proper categorization

### ✅ Complete Syllabus
- 358 semesters
- 1,790 subjects
- 8,950 units
- 26,850 sub-units

### ✅ Professional UI
- Dark mode support
- Responsive design
- Smooth animations
- Modern color scheme

### ✅ Real-time Search
- Course dropdown
- Semester auto-load
- Subject filtering
- Instant results

---

## 🛠️ Troubleshooting

### Backend not running?
```bash
cd backend
python run.py
```

### Frontend not running?
```bash
cd frontend
npm run dev
```

### Database issues?
```bash
# Reseed database
cd backend
python seed_database.py
```

### Port already in use?
- Backend: Change PORT in `.env`
- Frontend: Change port in `vite.config.js`

---

## 📖 Documentation

- **Main README**: `/README.md`
- **Setup Guide**: `/SETUP_GUIDE.md`
- **Implementation Details**: `/IMPLEMENTATION_COMPLETE.md`
- **Backend README**: `/backend/README.md`
- **Frontend README**: `/frontend/README.md`

---

## 🎓 Learning Resources

This project demonstrates:
- React 18 with Vite
- Flask REST API
- SQLAlchemy ORM
- JWT Authentication
- Tailwind CSS
- Framer Motion animations
- Zustand state management
- Responsive design

---

## 📞 Need Help?

1. Check the documentation files
2. Review error messages in console
3. Check browser developer tools (F12)
4. Review server logs

---

## 🎉 You're All Set!

Your KNU Student Syllabus Portal is ready to use!

**Start exploring:**
- 🏠 Home: http://localhost:3000/
- 📚 Dashboard: http://localhost:3000/dashboard (after login)
- 👤 Profile: http://localhost:3000/profile (after login)

**Enjoy! 🚀**

---

**Last Updated**: December 6, 2024
**Version**: 1.0.0
**Status**: ✅ Ready to Use
