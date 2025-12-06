# KNU Student Portal - Default Credentials

## 🔐 Demo Accounts

### Admin Account
```
Email: admin@knu.edu
Password: admin123
```
**Access**: Full admin dashboard with all features

### Student Account
```
Email: student@knu.edu
Password: student123
Roll Number: STU001
```
**Access**: Student dashboard and syllabus viewing

---

## 🚀 How to Use

### 1. **Database Setup**
Run the seed script to create default users:
```bash
cd backend
python seed_database.py
```

This will:
- Create both admin and student accounts
- Seed all 90 courses
- Create semesters, subjects, units, and sub-units
- Display confirmation messages for each account created

### 2. **Login Process**

#### Option A: Click Demo Card (Recommended)
1. Go to `/login` page
2. See "Demo Credentials" section with two cards
3. Click on either **Admin** or **Student** card
4. Form fields auto-fill with credentials
5. Click "Sign In" button

#### Option B: Manual Entry
1. Go to `/login` page
2. Enter email and password manually
3. Click "Sign In" button

### 3. **After Login**
- **Admin**: Redirected to `/admin` dashboard
- **Student**: Redirected to `/dashboard` with course and syllabus access

---

## 📋 Features

### Admin Features
- View all students
- Manage courses and semesters
- View activity logs
- System administration

### Student Features
- View enrolled courses
- Browse syllabus
- Search subjects
- View course materials
- Bookmark subjects

---

## 🔄 Reset Accounts

If you need to reset the demo accounts:

1. **Delete database**:
   ```bash
   rm instance/knu_portal.db
   ```

2. **Re-run seed script**:
   ```bash
   python seed_database.py
   ```

---

## ⚠️ Important Notes

- These are **demo accounts only** for testing purposes
- Do NOT use in production with these credentials
- Change passwords in production environment
- Admin account should have strong password
- Student account credentials are for testing only

---

## 🛠️ Troubleshooting

### Accounts Not Created
- Check if database exists: `instance/knu_portal.db`
- Run seed script again: `python seed_database.py`
- Check console output for error messages

### Login Failed
- Verify email and password are correct
- Check if backend server is running on `localhost:5000`
- Check browser console for API errors

### Can't Access Dashboard
- Ensure you're logged in (token in localStorage)
- Check if user type is correct (admin/student)
- Verify JWT token is valid

---

## 📞 Support

For issues or questions, check:
1. Backend logs in terminal
2. Browser console (F12)
3. Network tab for API responses
