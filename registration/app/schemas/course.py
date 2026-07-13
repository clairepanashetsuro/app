from pydantic import BaseModel

class Course(BaseModel): 
    name:str 
    department:str 
    description:str 
    is_online:bool 
    credit_hours:int 