#!/usr/bin/env python
"""
Automatic Fix Script for KNU Portal Login
This script fixes all login issues and sets up the database
"""

import os
import sys
import subprocess

def print_header(text):
    print("\n" + "="*60)
    print(f"  {text}")
    print("="*60)

def print_success(text):
    print(f"✅ {text}")

def print_error(text):
    print(f"❌ {text}")

def print_info(text):
    print(f"ℹ️  {text}")

def run_command(cmd, description):
    """Run a command and report status"""
    print_info(f"Running: {description}")
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print_success(description)
            return True
        else:
            print_error(f"{description} failed")
            print(result.stderr)
            return False
    except Exception as e:
        print_error(f"Error: {str(e)}")
        return False

def main():
    print_header("KNU PORTAL - AUTOMATIC LOGIN FIX")
    
    # Step 1: Check Python
    print_info("Checking Python installation...")
    try:
        import flask
        print_success("Python and Flask installed")
    except ImportError:
        print_error("Flask not installed. Installing...")
        run_command("pip install flask", "Installing Flask")
    
    # Step 2: Reset Database
    print_header("STEP 1: Resetting Database")
    try:
        from app import create_app, db
        from app.models import User, Student, Admin
        
        app = create_app()
        
        with app.app_context():
            print_info("Dropping all tables...")
            db.drop_all()
            print_success("Tables dropped")
            
            print_info("Creating all tables...")
            db.create_all()
            print_success("Tables created")
            
            print_info("Creating default users...")
            
            # Admin user
            admin_user = User(
                name='Admin',
                email='admin@knu.edu',
                phone='',
                user_type='admin'
            )
            admin_user.set_password('admin123')
            db.session.add(admin_user)
            db.session.flush()
            
            admin = Admin(user_id=admin_user.id)
            db.session.add(admin)
            db.session.commit()
            print_success("Admin user created: admin@knu.edu / admin123")
            
            # Student user
            student_user = User(
                name='Student',
                email='student@knu.edu',
                phone='',
                user_type='student'
            )
            student_user.set_password('student123')
            db.session.add(student_user)
            db.session.flush()
            
            student = Student(
                user_id=student_user.id,
                roll_number='STU001',
                father_name='Father Name'
            )
            db.session.add(student)
            db.session.commit()
            print_success("Student user created: student@knu.edu / student123")
            
    except Exception as e:
        print_error(f"Database setup failed: {str(e)}")
        return False
    
    # Step 3: Summary
    print_header("SETUP COMPLETE!")
    print_success("Database reset successfully")
    print_success("Default users created")
    
    print("\n" + "="*60)
    print("  LOGIN CREDENTIALS")
    print("="*60)
    print("\n  Admin Account:")
    print("  Email: admin@knu.edu")
    print("  Password: admin123")
    print("\n  Student Account:")
    print("  Email: student@knu.edu")
    print("  Password: student123")
    print("\n" + "="*60)
    
    print("\n📋 NEXT STEPS:")
    print("1. Start Backend: python run.py")
    print("2. Start Frontend: npm run dev")
    print("3. Open Browser: http://localhost:3000")
    print("4. Login with credentials above")
    print("5. Enjoy! 🎉")
    
    return True

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)) + '/backend')
    success = main()
    sys.exit(0 if success else 1)
