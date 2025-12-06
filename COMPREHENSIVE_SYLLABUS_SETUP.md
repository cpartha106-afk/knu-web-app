# 📚 সম্পূর্ণ বিস্তারিত সিলেবাস সিস্টেম

## ✅ কী তৈরি হয়েছে:

### 1. **বিস্তারিত সিলেবাস ডেটা**
- ৯০টি কোর্সের জন্য সম্পূর্ণ বিস্তারিত সিলেবাস
- প্রতিটি কোর্সে:
  - **থিওরি সাবজেক্ট**: মেজর, মাইনর, সাপোর্টিং
  - **প্র্যাক্টিক্যাল সাবজেক্ট**: ল্যাব ওয়ার্ক এবং এক্সপেরিমেন্ট
  - **বিস্তারিত বর্ণনা**: প্রতিটি সাবজেক্টের টপিক এবং ক্রেডিট
  - **ফোকাস এরিয়া**: কোর্সের মূল লক্ষ্য

### 2. **ব্যাকএন্ড API এন্ডপয়েন্ট**
```
GET /api/syllabus/course/<course_name>
- নির্দিষ্ট কোর্সের বিস্তারিত সিলেবাস

GET /api/syllabus/all-courses
- সব কোর্সের তালিকা

GET /api/syllabus/search?q=<query>
- কোর্স সার্চ করুন

GET /api/syllabus/categories
- কোর্স ক্যাটাগরি অনুযায়ী গ্রুপ করা

GET /api/syllabus/course/<course_name>/pdf
- PDF ডাউনলোড লিংক
```

### 3. **ফ্রন্টএন্ড পেজ**
- **DetailedSyllabus.jsx**: সম্পূর্ণ সিলেবাস ভিউ
  - Overview ট্যাব
  - Theory সাবজেক্ট ট্যাব
  - Practical সাবজেক্ট ট্যাব
  - Subjects ট্যাব
  - PDF ডাউনলোড বাটন

---

## 📊 কোর্স ডেটা স্ট্রাকচার:

### Bachelor Programs (15 কোর্স)
```
- Bachelor of Computer Application – BCA
- Bachelor of Computer Science – BCS
- Bachelor of Information Technology – B.Sc IT
- Bachelor of Software Engineering – BSE
- Bachelor of Data Science – BDS
- Bachelor of Computer Engineering – BCE
- Bachelor of Artificial Intelligence – BAI
- Bachelor of Cyber Security – BCS Cyber
- Bachelor of Cloud Computing – BCC
- Bachelor of Web Technology – BWT
- Bachelor of Mobile Application – BMA
- Bachelor of Network Technology – BNT
- Bachelor of Multimedia and Animation – BMAA
- Bachelor of Game Development – BGD
- Bachelor of Computer Graphics – BCG
```

### Master Programs (10 কোর্স)
```
- Master of Computer Application – MCA
- Master of Computer Science – MCS
- Master of Information Technology – M.Sc IT
- Master of Software Engineering – MSE
- Master of Data Science – MDS
- Master of Artificial Intelligence – MAI
- Master of Machine Learning – MML
- Master of Cloud Computing – MCC
- Master of Cyber Security – MCSec
- Master of Computer Networking – MCN
```

### Diploma Programs (25 কোর্স)
```
- Diploma in Computer Application – DCA
- Diploma in Information Technology – DIT
- Diploma in Software Engineering – DSE
- Diploma in Computer Engineering – DCE
- Diploma in Hardware and Networking – DHN
- Diploma in Computer Programming – DCP
- Diploma in Web Development – DWD
- Diploma in App Development – DAD
- Diploma in Game Development – DGD
- Diploma in Animation and VFX – DAVFX
- Diploma in Cyber Security – DCS
- Diploma in Cloud Computing – DCC
- Diploma in Data Science – DDS
- Diploma in Machine Learning – DML
- Diploma in Artificial Intelligence – DAI
- Diploma in Database Management – DDBM
- Diploma in Computer Networking – DCN
- Diploma in Computer Graphics – DCG
- Diploma in Full Stack Development – DFSD
- Diploma in UI UX Design – DUX
- Diploma in IT Support – DIS
- Diploma in Computer Hardware – DCH
- Diploma in Office Automation – DOA
- Diploma in Cloud Security – DCSec
- Diploma in Ethical Hacking – DEH
```

### Certificate Programs (30 কোর্স)
```
- Certificate in Computer Basics – CCB
- Certificate in MS Office – CMSO
- Certificate in Advanced Excel – CAE
- Certificate in Web Design – CWD
- Certificate in Frontend Development – CFD
- Certificate in Backend Development – CBD
- Certificate in Full Stack Development – CFSD
- Certificate in Python Programming – CPP
- Certificate in Java Programming – CJP
- Certificate in C Programming – CCP
- Certificate in C++ Programming – CCPP
- Certificate in SQL Database – CSD
- Certificate in Data Analysis – CDA
- Certificate in Artificial Intelligence – CAI
- Certificate in Machine Learning – CML
- Certificate in Cyber Security – CCS
- Certificate in Ethical Hacking – CEH
- Certificate in Cloud Computing – CCC
- Certificate in Networking – CN
- Certificate in Computer Typing – CCT
- Certificate in Tally with GST – CTG
- Certificate in Digital Marketing – CDM
- Certificate in Software Testing – CST
- Certificate in Mobile Repairing – CMR
- Certificate in Animation – CA
- Certificate in Video Editing – CVE
- Certificate in Graphic Design – CGD
- Certificate in Data Entry – CDE
- Certificate in Computer Accounting – CCA
- Certificate in Cloud Security – CCSec
```

### Advanced Diploma Programs (10 কোর্স)
```
- Advanced Diploma in Computer Application – ADCA
- Advanced Diploma in IT – ADIT
- Advanced Diploma in Software Engineering – ADSE
- Advanced Diploma in Web Engineering – ADWE
- Advanced Diploma in AI and ML – ADAIML
- Advanced Diploma in Cyber Security – ADCS
- Advanced Diploma in Cloud Computing – ADCC
- Advanced Diploma in Data Analytics – ADDA
- Advanced Diploma in Networking – ADN
- Advanced Diploma in Digital Forensics – ADDF
```

---

## 🚀 সেটআপ ধাপ:

### ধাপ 1: ব্যাকএন্ড ডাটাবেস রিসেট করুন
```bash
cd backend
python reset_db.py
```

### ধাপ 2: ব্যাকএন্ড শুরু করুন
```bash
python run.py
```

### ধাপ 3: ফ্রন্টএন্ড ডিপেন্ডেন্সি ইনস্টল করুন
```bash
cd frontend
npm install
```

### ধাপ 4: ফ্রন্টএন্ড শুরু করুন
```bash
npm run dev
```

### ধাপ 5: ব্রাউজারে যান
```
http://localhost:3000
```

---

## 📖 সিলেবাস কীভাবে অ্যাক্সেস করবেন:

### পদ্ধতি 1: কোর্স ক্যাটালগ থেকে
1. `/courses` পেজে যান
2. কোর্স খুঁজুন
3. "View Syllabus" বাটন ক্লিক করুন
4. বিস্তারিত সিলেবাস দেখুন

### পদ্ধতি 2: সরাসরি URL থেকে
```
http://localhost:3000/detailed-syllabus/Bachelor of Computer Application – BCA
```

### পদ্ধতি 3: API থেকে
```bash
curl http://localhost:5000/api/syllabus/course/Bachelor%20of%20Computer%20Application%20–%20BCA
```

---

## 📋 সিলেবাস বৈশিষ্ট্য:

### প্রতিটি কোর্সে:

#### থিওরি সাবজেক্ট:
- **মেজর সাবজেক্ট** (৬টি)
  - সম্পূর্ণ বর্ণনা
  - কোর্স কোড
  - ক্রেডিট
  - টপিক তালিকা

- **মাইনর সাবজেক্ট** (২টি)
  - বিস্তারিত তথ্য
  - প্রয়োজনীয় টপিক

- **সাপোর্টিং সাবজেক্ট** (২টি)
  - সহায়ক বিষয়
  - প্রয়োজনীয় জ্ঞান

#### প্র্যাক্টিক্যাল সাবজেক্ট:
- **মেজর প্র্যাক্টিক্যাল** (৩টি)
  - ল্যাব এক্সপেরিমেন্ট
  - হ্যান্ডস-অন প্রজেক্ট

- **মাইনর প্র্যাক্টিক্যাল** (১টি)
  - ক্যাপস্টোন প্রজেক্ট

- **সাপোর্টিং প্র্যাক্টিক্যাল** (১টি)
  - সেমিনার এবং প্রেজেন্টেশন

---

## 🎨 ইউজার ইন্টারফেস:

### সিলেবাস ভিউ পেজ:
- ✅ কোর্স শিরোনাম এবং কোড
- ✅ কোর্স ডিউরেশন
- ✅ ফোকাস এরিয়া
- ✅ ৪টি ট্যাব (Overview, Theory, Practical, Subjects)
- ✅ রঙিন কোডিং (মেজর-নীল, মাইনর-বেগুনি, সাপোর্টিং-সবুজ)
- ✅ PDF ডাউনলোড বাটন
- ✅ রেসপন্সিভ ডিজাইন
- ✅ ডার্ক মোড সাপোর্ট

---

## 📁 ফাইল তৈরি:

```
✅ backend/app/routes/comprehensive_courses_syllabus.py
   - সব কোর্সের বিস্তারিত ডেটা

✅ backend/app/routes/detailed_syllabus.py
   - API এন্ডপয়েন্ট

✅ frontend/src/pages/DetailedSyllabus.jsx
   - সিলেবাস ভিউ পেজ

✅ frontend/src/App.jsx (আপডেট)
   - নতুন রুট যোগ করা
```

---

## 🔍 API এন্ডপয়েন্ট:

### সব কোর্স পান
```bash
GET /api/syllabus/all-courses
```

### নির্দিষ্ট কোর্স সিলেবাস পান
```bash
GET /api/syllabus/course/Bachelor%20of%20Computer%20Application%20–%20BCA
```

### কোর্স সার্চ করুন
```bash
GET /api/syllabus/search?q=python
```

### ক্যাটাগরি অনুযায়ী পান
```bash
GET /api/syllabus/categories
```

---

## ✨ বৈশিষ্ট্য:

✅ **সম্পূর্ণ বিস্তারিত**: প্রতিটি কোর্সে সম্পূর্ণ সিলেবাস
✅ **অরিজিনাল কন্টেন্ট**: ডুপ্লিকেট মনে হয় না
✅ **পেশাদার ফরম্যাট**: পিডিএফের মতো দেখায়
✅ **সার্চ ফাংশনালিটি**: কোর্স খুঁজে পান সহজে
✅ **ক্যাটাগরি ফিল্টার**: ধরন অনুযায়ী ফিল্টার করুন
✅ **রেসপন্সিভ ডিজাইন**: সব ডিভাইসে কাজ করে
✅ **ডার্ক মোড**: চোখের জন্য আরামদায়ক
✅ **PDF ডাউনলোড**: সিলেবাস ডাউনলোড করুন

---

**সবকিছু প্রস্তুত! এখনই ব্যবহার করুন! 🚀**
