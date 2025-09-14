from app.models import df_students, df_scores, df_courses

# ========================
# get_student_report function
# ========================
def get_student_report(NIM, enrollment_year, PIN: str):
    # Validate student
    student = df_students[(df_students["NIM"] == NIM) &
                          (df_students["Enrollment Year"] == enrollment_year)]
    if student.empty:
        return {"error": "❌ Student not found"}
    
    student = student.iloc[0]
    if student["PIN"] != PIN:
        return {"error": "❌ Invalid PIN"}
    
    # Get latest academic record
    records = df_scores[df_scores["NIM"] == NIM]
    if records.empty:
        return {"error": "❌ No academic records found"}
    
    record = records.sort_values(by="Semester").iloc[-1]
    
    # Enrich courses with details
    course_list = []
    for c in record["Courses"]:
        course_info = df_courses[df_courses["Course ID"] == c["Course ID"]].iloc[0]
        course_list.append({
            "Course ID": course_info["Course ID"],
            "Course Name": course_info["Course Name"],
            "Lecturer": course_info["Lecturer"],
            "Credits": int(course_info["Credits"]),
            "Score": c["Score"]
        })
    
    return {
        "Student Name": student["Full Name"],
        "NIM": student["NIM"],
        "Semester": int(record["Semester"]),
        "Cumulative GPA": float(record["Cumulative GPA"]),
        "Semester GPA": float(record["Semester GPA"]),
        "Courses": course_list
    }

