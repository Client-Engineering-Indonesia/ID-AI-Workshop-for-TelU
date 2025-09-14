from fastapi import FastAPI
from sis_app.app.student import get_student_info
from sis_app.app.report import get_student_report
from sis_app.app.schedule import get_my_schedule

app = FastAPI(title="Telkom University SIS API", version="1.0.0")

@app.get("/")
def root():
    return {"message": "Welcome to Telkom University SIS API"}

@app.get("/student/info")
def api_student_info(NIM: str, enrollment_year: int, PIN: str):
    """
    Retrieve detailed information about a student.

    Parameters:
        NIM (str): Student ID number.
        enrollment_year (int): Year the student enrolled.
        PIN (str): Secret PIN number for authentication.

    Returns:
        dict: Student information including name, NIM, enrollment year, 
              year, term, field of study, and academic advisor.
    """
    return get_student_info(NIM, enrollment_year, PIN)


@app.get("/student/report")
def api_student_report(NIM: str, enrollment_year: int, PIN: str):
    """
    Retrieve the academic report of a student.

    Parameters:
        NIM (str): Student ID number.
        enrollment_year (int): Year the student enrolled.
        PIN (str): Secret PIN number for authentication.

    Returns:
        dict: Academic report including student name, NIM, semester,
              cumulative GPA, semester GPA, and a list of enrolled courses 
              with course details (Course ID, Course Name, Lecturer, Credits, Score).
    """
    return get_student_report(NIM, enrollment_year, PIN)


@app.get("/student/schedule")
def api_student_schedule(NIM: str, enrollment_year: int, PIN: str):
    """
    Retrieve the weekly class schedule of a student.

    Parameters:
        NIM (str): Student ID number.
        enrollment_year (int): Year the student enrolled.
        PIN (str): Secret PIN number for authentication.

    Returns:
        dict: Student schedule including name, NIM, semester, and 
              a weekly timetable grouped by day (Monday–Friday).
              Each day contains a list of course details (Course ID, 
              Course Name, Day, Time, Room, Lecturer).
    """
    return get_my_schedule(NIM, enrollment_year, PIN)

