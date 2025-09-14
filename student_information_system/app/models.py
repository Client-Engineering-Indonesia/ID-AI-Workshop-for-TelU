import pandas as pd

# ========================
# Students Data
# ========================
students_data = [
    {"Full Name": "Rizky Pratama", "NIM": "110123001", "Enrollment Year": 2023,
     "Year": 2, "Term": 4, "Field of Study": "Informatics Engineering",
     "Academic Advisor": "Dr. Andi Setiawan", "PIN": "1234"},
    
    {"Full Name": "Ayu Lestari Putri", "NIM": "110124015", "Enrollment Year": 2024,
     "Year": 1, "Term": 2, "Field of Study": "Visual Communication Design",
     "Academic Advisor": "Dr. Maya Kartika", "PIN": "2345"},
    
    {"Full Name": "Muhammad Fajar Ramadhan", "NIM": "110122043", "Enrollment Year": 2022,
     "Year": 3, "Term": 6, "Field of Study": "Electrical Engineering",
     "Academic Advisor": "Prof. Bambang Santoso", "PIN": "3456"},
    
    {"Full Name": "Dwi Ananda Kusuma", "NIM": "110121078", "Enrollment Year": 2021,
     "Year": 4, "Term": 8, "Field of Study": "Industrial Engineering",
     "Academic Advisor": "Dr. Rina Yuliana", "PIN": "4567"},
    
    {"Full Name": "Siti Nurhaliza", "NIM": "110123056", "Enrollment Year": 2023,
     "Year": 2, "Term": 3, "Field of Study": "Information Systems",
     "Academic Advisor": "Dr. Ahmad Firmansyah", "PIN": "5678"},
]

df_students = pd.DataFrame(students_data)

# ========================
# Courses Data
# ========================
courses_data = [
    # Informatics Engineering
    {"Course Name": "Data Structures", "Course ID": "INF101", "Credits": 3, "Lecturer": "Dr. Andi Setiawan", "Field": "Informatics Engineering"},
    {"Course Name": "Database Systems", "Course ID": "INF102", "Credits": 3, "Lecturer": "Dr. Budi Santoso", "Field": "Informatics Engineering"},
    # Visual Communication Design
    {"Course Name": "Graphic Design Basics", "Course ID": "DSN201", "Credits": 3, "Lecturer": "Dr. Maya Kartika", "Field": "Visual Communication Design"},
    {"Course Name": "Digital Illustration", "Course ID": "DSN202", "Credits": 2, "Lecturer": "Dr. Yuli Handayani", "Field": "Visual Communication Design"},
    # Electrical Engineering
    {"Course Name": "Circuit Theory", "Course ID": "ELC301", "Credits": 3, "Lecturer": "Prof. Bambang Santoso", "Field": "Electrical Engineering"},
    {"Course Name": "Electromagnetics", "Course ID": "ELC302", "Credits": 3, "Lecturer": "Dr. Wahyu Gunawan", "Field": "Electrical Engineering"},
    # Industrial Engineering
    {"Course Name": "Operations Research", "Course ID": "IND401", "Credits": 3, "Lecturer": "Dr. Rina Yuliana", "Field": "Industrial Engineering"},
    {"Course Name": "Supply Chain Management", "Course ID": "IND402", "Credits": 3, "Lecturer": "Dr. Suryo Adi", "Field": "Industrial Engineering"},
    # Information Systems
    {"Course Name": "System Analysis and Design", "Course ID": "IS501", "Credits": 3, "Lecturer": "Dr. Ahmad Firmansyah", "Field": "Information Systems"},
    {"Course Name": "Business Intelligence", "Course ID": "IS502", "Credits": 3, "Lecturer": "Dr. Lina Marlina", "Field": "Information Systems"},
]

df_courses = pd.DataFrame(courses_data)

# ========================
# GPA + Scores Data
# ========================
scores_data = [
    {"NIM": "110123001", "Semester": 4, "Cumulative GPA": 3.45, "Semester GPA": 3.60,
     "Courses": [
         {"Course ID": "INF101", "Score": "A"},
         {"Course ID": "INF102", "Score": "B+"},
         {"Course ID": "IS501", "Score": "A"},
         {"Course ID": "IS502", "Score": "A-"},
     ]},
    {"NIM": "110124015", "Semester": 2, "Cumulative GPA": 3.70, "Semester GPA": 3.80,
     "Courses": [
         {"Course ID": "DSN201", "Score": "A"},
         {"Course ID": "DSN202", "Score": "A"},
         {"Course ID": "INF101", "Score": "B"},
         {"Course ID": "INF102", "Score": "B+"},
     ]},
]
df_scores = pd.DataFrame(scores_data)

# ========================
# Weekly Schedule Data
# ========================
schedule_data = [
    {"Course ID": "INF101", "Day": "Monday", "Time": "08:00-09:40", "Room": "A101"},
    {"Course ID": "INF102", "Day": "Wednesday", "Time": "10:00-11:40", "Room": "B202"},
    {"Course ID": "DSN201", "Day": "Tuesday", "Time": "13:00-14:40", "Room": "D303"},
    {"Course ID": "DSN202", "Day": "Thursday", "Time": "09:00-10:40", "Room": "D305"},
    {"Course ID": "ELC301", "Day": "Monday", "Time": "13:00-14:40", "Room": "E101"},
    {"Course ID": "ELC302", "Day": "Friday", "Time": "08:00-09:40", "Room": "E102"},
    {"Course ID": "IND401", "Day": "Tuesday", "Time": "10:00-11:40", "Room": "F201"},
    {"Course ID": "IND402", "Day": "Thursday", "Time": "13:00-14:40", "Room": "F202"},
    {"Course ID": "IS501", "Day": "Wednesday", "Time": "08:00-09:40", "Room": "G101"},
    {"Course ID": "IS502", "Day": "Friday", "Time": "13:00-14:40", "Room": "G102"},
]

df_schedule = pd.DataFrame(schedule_data)
