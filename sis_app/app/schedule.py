from app.models import df_students, df_schedule, df_enrollments, df_courses

def get_my_schedule(NIM: str, enrollment_year: int, PIN: str):
    # Validate student
    student = df_students[(df_students["NIM"] == NIM) &
                          (df_students["Enrollment Year"] == enrollment_year) &
                          (df_students["PIN"] == PIN)]
    if student.empty:
        return {"error": "Invalid student credentials"}
    
    student_name = student.iloc[0]["Full Name"]

    # Get current enrollments
    enrollments = df_enrollments[df_enrollments["NIM"] == NIM]
    if enrollments.empty:
        return {"error": "No enrollments found for this student"}
    
    course_ids = [c["Course ID"] for c in enrollments.iloc[0]["Courses"]]

    # Join with schedule and course info
    schedule = (df_schedule.merge(df_courses, on="Course ID", how="left")
                           .query("`Course ID` in @course_ids")
                           [["Course ID", "Course Name", "Day", "Time", "Room", "Lecturer"]])

    # Build grouped schedule by day
    grouped_schedule = {}
    for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
        day_courses = schedule[schedule["Day"] == day].sort_values(by="Time")
        if not day_courses.empty:
            grouped_schedule[day.lower()] = day_courses.to_dict(orient="records")

    return {
        "Student": student_name,
        "NIM": NIM,
        "Semester": int(student.iloc[0]["Term"]),
        "Schedule": grouped_schedule
    }


