from fastapi import FastAPI 
from pydantic import BaseModel 
from database import (
    create_table,
    add_student, get_students, update_student, delete_student,
    add_teacher, get_teachers, update_teacher, delete_teacher,
    add_course, get_courses, update_course, delete_course
) 

app = FastAPI() 

@app.on_event("startup")
def startup_event():
    create_table()

@app.get( "/" ) 
def home(): 
    return { "message" : "welcome to my first api server" } 

class Student(BaseModel): 
    name:str 
    age:int 
    email:str 
    country:str 
    id_number:int 

@app.post( "/students" ) 
def register_students(student:Student): 
    add_student(student.name,student.age,student.email, student.country,student.id_number) 
    return student 

@app.get( "/students" ) 
def list_students(): 
    students=get_students() 
    return students

@app.put( "/students/{id_number}" )
def edit_student(id_number: int, student: Student):
    update_student(id_number, student.name, student.age, student.email, student.country)
    return {"message": f"Student {id_number} updated successfully", "data": student}

@app.delete( "/students/{id_number}" )
def remove_student(id_number: int):
    delete_student(id_number)
    return {"message": f"Student {id_number} deleted successfully"}

class Teacher(BaseModel): 
    name:str 
    age:int 
    email:str 
    country:str 
    id_number:int 

@app.post( "/teacher" ) 
def register_teachers(teacher:Teacher): 
    add_teacher(teacher.name,teacher.age,teacher.email, teacher.country,teacher.id_number) 
    return teacher 

@app.get( "/teachers" ) 
def list_teachers(): 
    teacher=get_teachers() 
    return teacher

@app.put( "/teacher/{id_number}" )
def edit_teacher(id_number: int, teacher: Teacher):
    update_teacher(id_number, teacher.name, teacher.age, teacher.email, teacher.country)
    return {"message": f"Teacher {id_number} updated successfully", "data": teacher}

@app.delete( "/teacher/{id_number}" )
def remove_teacher(id_number: int):
    delete_teacher(id_number)
    return {"message": f"Teacher {id_number} deleted successfully"}

class Course(BaseModel): 
    name:str 
    department:str 
    description:str 
    is_online:bool 
    credit_hours:int 

@app.post( "/course" ) 
def register_courses(course:Course): 
    add_course(course.name,course.department,course.description, course.is_online,course.credit_hours) 
    return course 

@app.get( "/courses" ) 
def list_courses(): 
    course=get_courses() 
    return course

@app.put( "/course/{name}" )
def edit_course(name: str, course: Course):
    update_course(name, course.department, course.description, course.is_online, course.credit_hours)
    return {"message": f"Course '{name}' updated successfully", "data": course}

@app.delete( "/course/{name}" )
def remove_course(name: str):
    delete_course(name)
    return {"message": f"Course '{name}' deleted successfully"}
