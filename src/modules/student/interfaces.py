from pydantic import Field, EmailStr, BaseModel

class StudentCreate(BaseModel):
    name : str
    age : int
    email : EmailStr
    ph_no : str = Field(max_length = 10, min_length=10, pattern = r"^[6-9]\d{9}$")


class StudentUpdate(BaseModel):
    stu_id: int
    name : str
    age : int
    email : EmailStr
    ph_no : str = Field(max_length = 10, min_length=10, pattern = r"^[6-9]\d{9}$")

    class config:
        form_attributes = True