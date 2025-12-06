# 🚨 FIX LOGIN ERROR - IMMEDIATE SOLUTION

## ❌ Problem
Login is failing with: "Login failed. Please try again."

## ✅ Solution - 3 Steps

### Step 1: Reset Database
```bash
cd backend
python reset_db.py
```

**Output should show:**
```
[SUCCESS] Database reset completed!
Admin:   admin@knu.edu / admin123
Student: student@knu.edu / student123
```

### Step 2: Restart Backend
```bash
python run.py
```

**Wait for message:**
```
Running on http://127.0.0.1:5000
```

### Step 3: Login
1. Go to: `http://localhost:3000`
2. Click **Student** card (green)
3. Email: `student@knu.edu`
4. Password: `student123`
5. Click **Sign In**

---

## 🎯 Expected Result
✅ Login successful
✅ Redirected to dashboard
✅ Navigation bar visible
✅ Welcome message displayed

---

## 📋 Credentials Ready to Use

### Admin
```
Email: admin@knu.edu
Password: admin123
```

### Student
```
Email: student@knu.edu
Password: student123
```

---

## ⚡ Quick Commands

```bash
# Terminal 1 - Backend
cd backend
python reset_db.py
python run.py

# Terminal 2 - Frontend
cd frontend
npm run dev

# Browser
http://localhost:3000
```

---

**That's it! You're ready to login! 🎉**
