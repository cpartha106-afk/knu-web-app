# 🚀 KNU Portal - Quick Login Guide

## ⚡ Get Started in 3 Steps

### Step 1: Start Backend Server
```bash
cd backend
python run.py
```
✅ Backend runs on: `http://localhost:5000`

### Step 2: Start Frontend Server
```bash
cd frontend
npm run dev
```
✅ Frontend runs on: `http://localhost:3000`

### Step 3: Seed Database with Default Users
```bash
cd backend
python seed_database.py
```
✅ Creates demo accounts automatically

---

## 🔐 Default Login Credentials

### Option 1: Admin Account
```
Email: admin@knu.edu
Password: admin123
```
**Access**: Full admin dashboard with all management features

### Option 2: Student Account
```
Email: student@knu.edu
Password: student123
```
**Access**: Student dashboard with course and syllabus features

---

## 📱 How to Login

### Method 1: Click Demo Card (Easiest)
1. Go to `http://localhost:3000/login`
2. See "Demo Credentials" section with two colored cards
3. Click on **Admin** or **Student** card
4. Form auto-fills with credentials
5. Click "Sign In" button
6. ✅ Redirected to dashboard

### Method 2: Manual Entry
1. Go to `http://localhost:3000/login`
2. Enter email and password manually
3. Click "Sign In" button
4. ✅ Redirected to dashboard

---

## 🎯 After Login

### Admin Dashboard
- View all students
- Manage courses and semesters
- View system analytics
- Access admin settings

### Student Dashboard
- View enrolled courses
- Browse syllabus
- Search subjects
- View course materials
- Access student profile

---

## 🧭 Navigation Bar Features

The top navigation bar includes:

### 📚 Academics (10 sub-features)
- My Courses
- Syllabus
- Semesters
- Subjects
- Study Materials
- Assignments
- Exam Schedule
- Results
- Attendance
- Grade Card

### 👤 Profile (10 sub-features)
- My Profile
- Edit Profile
- Change Password
- Personal Info
- Contact Details
- Emergency Contact
- Address
- Documents
- Preferences
- Privacy Settings

### 📊 Reports (10 sub-features)
- Academic Report
- Performance
- Transcript
- Certificates
- Fee Status
- Attendance Report
- Course Progress
- Semester Report
- Achievements
- Activity Log

### ⚙️ Settings (10 sub-features)
- General Settings
- Notifications
- Email Preferences
- Privacy
- Security
- Two-Factor Auth
- Connected Devices
- Theme
- Language
- Accessibility

### ❓ Help (10 sub-features)
- FAQ
- Documentation
- Contact Support
- Report Issue
- Feedback
- Tutorials
- Video Guides
- Troubleshooting
- About Us
- Terms & Conditions

---

## 🎨 UI Features

✅ **Professional Navigation Bar**
- Gradient background (Blue → Purple)
- Dropdown menus with 10 sub-features each
- Theme toggle (Light/Dark mode)
- Notification bell
- User profile section
- Logout button

✅ **Responsive Design**
- Works on desktop, tablet, mobile
- Smooth animations
- Dark mode support
- Accessible UI

✅ **Professional Dashboard**
- Welcome section
- Quick stats
- Search functionality
- Course materials
- Syllabus viewer

---

## ⚠️ Troubleshooting

### Login Failed
- ✅ Check backend is running on port 5000
- ✅ Check frontend is running on port 3000
- ✅ Verify email and password are correct
- ✅ Check browser console for errors (F12)

### Database Issues
- ✅ Delete `backend/instance/knu_portal.db`
- ✅ Run `python seed_database.py` again
- ✅ Restart both servers

### Port Already in Use
- ✅ Backend: Change port in `backend/.env`
- ✅ Frontend: Change port in `frontend/vite.config.js`

---

## 📋 Checklist

- [ ] Backend running on port 5000
- [ ] Frontend running on port 3000
- [ ] Database seeded with demo users
- [ ] Can access login page
- [ ] Can login with demo credentials
- [ ] Dashboard loads successfully
- [ ] Navigation bar visible
- [ ] Dropdown menus work
- [ ] Theme toggle works
- [ ] Can logout

---

## 🎓 Demo Data

The system comes with:
- ✅ 90 Courses (15 Bachelor, 10 Master, 25 Diploma, 30 Certificate, 10 Advanced Diploma)
- ✅ 358 Semesters
- ✅ 1,790 Subjects
- ✅ 8,950 Units
- ✅ 26,850 Sub-Units

---

## 🚀 You're All Set!

1. ✅ Start backend: `python run.py`
2. ✅ Start frontend: `npm run dev`
3. ✅ Seed database: `python seed_database.py`
4. ✅ Open browser: `http://localhost:3000`
5. ✅ Login with demo credentials
6. ✅ Explore the dashboard!

**Happy Learning! 🎉**

---

**Need Help?** Check the detailed setup guide: `SETUP_GUIDE.md`
