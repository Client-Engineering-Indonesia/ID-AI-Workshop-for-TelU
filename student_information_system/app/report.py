from app.models import df_students, df_records, df_gpa

def get_student_report(NIM, enrollment_year, PIN, semester=None):
    student = df_students[(df_students["NIM"] == NIM) &
                          (df_students["Enrollment Year"] == enrollment_year)]
    if student.empty:
        return {"error": "❌ Student not found."}
    student = student.iloc[0]

    if student["PIN"] != PIN:
        return {"error": "❌ Invalid PIN."}

    sem = semester if semester else student["Term"]

    student_courses = df_records[(df_records["NIM"] == NIM) &
                                 (df_records["Semester"] == sem)]

    if student_courses.empty:
        return {"error": f"No report found for semester {sem}"}

    gpa = df_gpa[df_gpa["NIM"] == NIM]["Cumulative GPA"].values[0]
    sem_gpa = round((student_courses["Grade Point"] * student_courses["Credits"]).sum()
                    / student_courses["Credits"].sum(), 2)

    return {
        "Full Name": student["Full Name"],
        "NIM": student["NIM"],
        "Enrollment Year": student["Enrollment Year"],
        "Semester": sem,
        "Field of Study": student["Field of Study"],
        "Academic Advisor": student["Academic Advisor"],
        "Semester GPA": sem_gpa,
        "Cumulative GPA": gpa,
        "Courses": student_courses.to_dict(orient="records")
    }
