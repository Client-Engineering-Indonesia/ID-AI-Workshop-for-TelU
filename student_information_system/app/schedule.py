from app.models import df_students, df_schedule

def get_my_schedule(NIM, enrollment_year, PIN, semester=None):
    student = df_students[(df_students["NIM"] == NIM) &
                          (df_students["Enrollment Year"] == enrollment_year)]
    if student.empty:
        return {"error": "❌ Student not found."}
    student = student.iloc[0]

    if student["PIN"] != PIN:
        return {"error": "❌ Invalid PIN."}

    sem = semester if semester else student["Term"]

    schedule = df_schedule[(df_schedule["NIM"] == NIM) &
                           (df_schedule["Semester"] == sem)]

    if schedule.empty:
        return {"error": f"No schedule found for semester {sem}"}

    return {
        "Full Name": student["Full Name"],
        "NIM": student["NIM"],
        "Semester": sem,
        "Weekly Schedule": schedule.to_dict(orient="records")
    }
