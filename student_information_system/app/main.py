from fastapi import FastAPI
from app.student import get_student_info
from app.report import get_student_report
from app.schedule import get_my_schedule

app = FastAPI(title="Telkom University SIS API", version="1.0.0")

@app.get("/")
def root():
    return {"message": "Welcome to Telkom University SIS API"}

@app.get("/student/info")
def api_student_info(NIM: str, enrollment_year: int, PIN: str):
    return get_student_info(NIM, enrollment_year, PIN)

@app.get("/student/report")
def api_student_report(NIM: str, enrollment_year: int, PIN: str, semester: int = None):
    return get_student_report(NIM, enrollment_year, PIN, semester)

@app.get("/student/schedule")
def api_student_schedule(NIM: str, enrollment_year: int, PIN: str, semester: int = None):
    return get_my_schedule(NIM, enrollment_year, PIN, semester)
