from fastapi import APIRouter 

from schemas.student import Student

from repositories.student import(
    add_student,
    get_students,
    update_student,
    delete_student,

)

router = APIRouter(prefix = "/students", tags = ["students"])

@router.post( "" ) 
def register_students(student:Student): 
    add_student(student.name,student.age,student.email, student.country,student.id_number) 
    return student 

@router.get( "" ) 
def list_students(): 
    students=get_students() 
    return students

@router.put( "/{id_number}" )
def edit_student(id_number: int, student: Student):
    update_student(id_number, student.name, student.age, student.email, student.country)
    return {"message": f"Student {id_number} updated successfully", "data": student}

@router.delete( "/{id_number}" )
def remove_student(id_number: int):
    delete_student(id_number)
    return {"message": f"Student {id_number} deleted successfully"}