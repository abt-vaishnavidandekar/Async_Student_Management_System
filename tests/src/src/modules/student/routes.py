from fastapi import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from src.modules.student.functions import get_students, create_student, update_student, delete_student
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.configs.model import get_db
from .interfaces import StudentCreate, StudentUpdate



# Configured Router for Authentication Routes for User
student_router = APIRouter(prefix="/student")



# Router Function to Handle User Login POST Request

@student_router.get("/")
async def get_all_students(db: AsyncSession = Depends(get_db)):
    return await get_students(db)

@student_router.post("/create")
async def create_one_student(student : StudentCreate, db: AsyncSession = Depends(get_db)):
    return await create_student(student, db)

@student_router.put("/update")
async def update_student_route( student : StudentUpdate, db: AsyncSession = Depends(get_db)):
    return await update_student(db=db, student_data=student)
    
@student_router.delete("/delete/{student_id}")
async def delete_student_route(student_id : int, db: AsyncSession = Depends(get_db)):
    return await delete_student(student_id, db)