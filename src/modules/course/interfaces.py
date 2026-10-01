from pydantic import  BaseModel

class CreateCourse(BaseModel):
    name : str
    description : str
    instructor_id : int