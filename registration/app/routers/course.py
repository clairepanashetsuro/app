from fastapi import APIRouter

from schemas.course import Course

from repositories.course import(
    add_course,
    get_courses,
    update_course,
    delete_course,

)

router = APIRouter(prefix = "/courses", tags = ["course"])

@router.post( "" ) 
def register_courses(course:Course): 
    add_course(course.name,course.department,course.description, course.is_online,course.credit_hours) 
    return course 

@router.get( "" ) 
def list_courses(): 
    course=get_courses() 
    return course

@router.put( "/{name}" )
def edit_course(name: str, course: Course):
    update_course(name, course.department, course.description, course.is_online, course.credit_hours)
    return {"message": f"Course '{name}' updated successfully", "data": course}

@router.delete( "/{name}" )
def remove_course(name: str):
    delete_course(name)
    return {"message": f"Course '{name}' deleted successfully"}

