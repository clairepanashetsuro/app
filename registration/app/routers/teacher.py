from fastapi import APIRouter

from schemas.teacher import Teacher

from repositories.teacher import(
    add_teacher,
    get_teachers,
    update_teacher,
    delete_teacher,

)

router = APIRouter(prefix = "/teachers", tags = ["teachers"])

@router.post( "" ) 
def register_teachers(teacher:Teacher): 
    add_teacher(teacher.name,teacher.age,teacher.email, teacher.country,teacher.id_number) 
    return teacher 

@router.get( "" ) 
def list_teachers(): 
    teacher=get_teachers() 
    return teacher

@router.put( "/{id_number}" )
def edit_teacher(id_number: int, teacher: Teacher):
    update_teacher(id_number, teacher.name, teacher.age, teacher.email, teacher.country)
    return {"message": f"Teacher {id_number} updated successfully", "data": teacher}

@router.delete( "/{id_number}" )
def remove_teacher(id_number: int):
    delete_teacher(id_number)
    return {"message": f"Teacher {id_number} deleted successfully"}
