from student_information_system.app.models import df_students

def get_student_info(NIM, enrollment_year, PIN):
    student = df_students[(df_students["NIM"] == NIM) &
                          (df_students["Enrollment Year"] == enrollment_year)]
    if student.empty:
        return {"error": "❌ Student not found."}
    student = student.iloc[0]

    if student["PIN"] != PIN:
        return {"error": "❌ Invalid PIN."}

    return {
        "Full Name": student["Full Name"],
        "NIM": student["NIM"],
        "Enrollment Year": student["Enrollment Year"],
        "Current Year": student["Current Year"],
        "Semester": student["Term"],
        "Field of Study": student["Field of Study"],
        "Academic Advisor": student["Academic Advisor"]
    }
