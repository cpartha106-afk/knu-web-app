# Testing the Course Catalog & Syllabus System

## Quick Test Guide

### 1. Test Backend API Endpoints

#### Test Get All Courses
```bash
curl http://localhost:5000/api/syllabus/all-courses
```

Expected Response:
```json
{
  "courses": [
    "Bachelor of Computer Application",
    "Bachelor of Computer Science",
    ...
  ],
  "total": 90
}
```

#### Test Get Course Syllabus
```bash
curl "http://localhost:5000/api/syllabus/course/Bachelor%20of%20Computer%20Application"
```

Expected Response:
```json
{
  "title": "Bachelor of Computer Application (BCA)",
  "duration": "3 Years",
  "semesters": 6,
  "overview": "A comprehensive three-year undergraduate program...",
  "theory_subjects": [...],
  "practical_subjects": [...]
}
```

### 2. Test Frontend Features

#### A. Register Page - Course Dropdown
1. Navigate to: `http://localhost:3000/register`
2. Click "Next" to go to Step 2
3. Check "Course" dropdown
4. Verify all 90 courses are listed
5. Verify courses are organized by category (optgroup)

**Expected:**
- Bachelor Programs (15 courses)
- Master Programs (10 courses)
- Diploma Programs (25 courses)
- Certificate Programs (30 courses)
- Advanced Diploma Programs (10 courses)

#### B. Course Catalog Page
1. Navigate to: `http://localhost:3000/courses`
2. Verify all 90 courses are displayed
3. Test search functionality:
   - Search "Python" → Should show Python-related courses
   - Search "Cloud" → Should show Cloud-related courses
4. Test category filters:
   - Click "Bachelor" → Should show 15 courses
   - Click "Master" → Should show 10 courses
   - Click "Diploma" → Should show 25 courses
   - Click "Certificate" → Should show 30 courses
   - Click "Advanced Diploma" → Should show 10 courses
5. Click on any course card → Should navigate to syllabus page

#### C. Syllabus View Page
1. From course catalog, click on "Bachelor of Computer Application"
2. Verify page displays:
   - Course title and duration
   - Number of semesters
   - Program overview
   - Course statistics (Duration, Semesters, Subjects)
3. Click "Theory Subjects" tab:
   - Should show all theory subjects
   - Each subject should have: name, code, credits, type, units
4. Click "Practical Subjects" tab:
   - Should show all practical subjects
   - Each subject should have: name, code, credits, type, experiments
5. Click "Overview" tab:
   - Should show program structure summary

### 3. Test Data Validation

#### Verify Course Count
- Total courses should be: **90**
  - Bachelor: 15
  - Master: 10
  - Diploma: 25
  - Certificate: 30
  - Advanced: 10

#### Verify Course Names
Sample courses that should exist:
- Bachelor of Computer Application – BCA
- Master of Computer Application – MCA
- Diploma in Computer Application – DCA
- Certificate in Python Programming – CPP
- Advanced Diploma in AI and ML – ADAIML

#### Verify Syllabus Structure
Each course should have:
- ✅ Title
- ✅ Duration
- ✅ Number of Semesters
- ✅ Overview/Description
- ✅ Theory Subjects (at least 4-5)
- ✅ Practical Subjects (at least 2-3)
- ✅ Each subject has units/experiments

### 4. Test User Registration with Course

1. Navigate to: `http://localhost:3000/register`
2. Fill Step 1:
   - Full Name: Test Student
   - Father's Name: Test Father
   - Phone: 9876543210
3. Click "Next"
4. Fill Step 2:
   - Roll Number: TEST001
   - Course: Select "Bachelor of Computer Application"
   - Semester: Select "Semester 1"
5. Click "Next"
6. Fill Step 3:
   - Email: test@example.com
   - Password: Test@123
   - Confirm Password: Test@123
7. Click "Create Account"
8. Verify registration is successful

### 5. Performance Tests

#### Load Test - Course Catalog
1. Navigate to `/courses`
2. Verify page loads in < 2 seconds
3. Verify all 90 courses render smoothly
4. Test search with multiple keywords
5. Test rapid category switching

#### Load Test - Syllabus View
1. Navigate to `/syllabus/Bachelor%20of%20Computer%20Application`
2. Verify page loads in < 2 seconds
3. Verify all sections render correctly
4. Test tab switching (Overview → Theory → Practical)

### 6. Browser Compatibility

Test on:
- ✅ Chrome/Chromium
- ✅ Firefox
- ✅ Safari
- ✅ Edge

### 7. Responsive Design Tests

Test on:
- ✅ Desktop (1920x1080)
- ✅ Tablet (768x1024)
- ✅ Mobile (375x667)

Verify:
- Course cards stack properly
- Search bar is accessible
- Dropdowns work on mobile
- Text is readable on all sizes

## Expected Results

### ✅ All Tests Should Pass
- All 90 courses visible in register dropdown
- All 90 courses visible in course catalog
- Search functionality works correctly
- Category filters work correctly
- Syllabus displays correctly with theory and practical subjects
- User can register with any of the 90 courses
- Page loads quickly and smoothly
- Responsive on all devices

## Troubleshooting

### Issue: Courses not showing in dropdown
**Solution:** 
- Check if backend is running on port 5000
- Check if `comprehensive_syllabus.py` is properly imported
- Clear browser cache and reload

### Issue: Syllabus page shows error
**Solution:**
- Check if course name is URL encoded properly
- Check browser console for API errors
- Verify backend API endpoint is working

### Issue: Search not working
**Solution:**
- Check if JavaScript is enabled
- Check browser console for errors
- Verify search term is being entered correctly

### Issue: Animations not smooth
**Solution:**
- Check if Framer Motion is installed
- Check browser performance
- Try disabling browser extensions

## Success Criteria

✅ All 90 courses are available in the system
✅ Courses are properly categorized
✅ Syllabus displays with theory and practical subjects
✅ Search and filter functionality works
✅ User can register with any course
✅ Pages load quickly and smoothly
✅ Responsive design works on all devices
✅ No console errors or warnings

## Status: READY FOR TESTING ✅
