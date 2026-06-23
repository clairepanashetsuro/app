from fastapi import FastAPI
from pydantic import BaseModel
from database import create_table,add_student,get_students, add_teacher,get_teachers,add_course,get_courses
app = FastAPI()
@app.get("/")
def home():
    return {"message": "welcome to my first api server"}

class Student(BaseModel):
    name:str
    age:int
    email:str
    country:str
    id_number:int

@app.post("/students") 
def register_students(student:Student):
    add_student(student.name,student.age,student.email, student.country,student.id_number)
    return student

@app.get("/students")
def list_students():
    students=get_students()
    return students

class Teacher(BaseModel):
    name:str
    age:int
    email:str
    country:str
    id_number:int

@app.post("/teacher") 
def register_teachers(teacher:Teacher):
    add_teacher(teacher.name,teacher.age,teacher.email, teacher.country,teacher.id_number)
    return teacher

@app.get("/teachers")
def list_teachers():
    teacher=get_teachers()
    return teacher

class Course(BaseModel):
    name:str
    department:str
    description:str
    is_online:bool
    credit_hours:int

@app.post("/course") 
def register_courses(course:Course):
    add_course(course.name,course.department,course.description, course.is_online,course.credit_hours)
    return course

@app.get("/courses")
def list_courses():
    course=get_courses()
    return course


