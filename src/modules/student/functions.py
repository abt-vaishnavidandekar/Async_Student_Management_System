from fastapi import status
from fastapi.responses import JSONResponse
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from .models import Student
from .interfaces import StudentCreate, StudentUpdate
from src.configs.model import engine, Base




# User Function to Handle User Login POST Request
async def user_login_post() -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"success": True, "message": "Login successful"},
    )


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def get_students(db : AsyncSession):
    result = await db.execute(select(Student))
    students = result.scalars().all()

    return students

async def create_student(student : StudentCreate, db : AsyncSession):
    new_student = Student(
        name = student.name,
        age = student.age,
        email = student.email,
        ph_no = student.ph_no
    )

    db.add(new_student)
    await db.commit()
    await db.refresh(new_student)

    return new_student


async def update_student(student_data: StudentUpdate, db: AsyncSession):

    try: 
        student_fetch_query = await db.execute(
            select(Student).where(Student.stu_id == student_data.stu_id)
        )
        student = student_fetch_query.scalar_one_or_none()
        if not student:
            return "Not found"


        student.name = student_data.name
        student.age = student_data.age
        student.email = student_data.email
        student.ph_no = student_data.ph_no

        await db.commit()

        await db.refresh(student)

        return student

    except:
        import traceback
        traceback.print_exc()
        raise


async def delete_student(student_id : int, db: AsyncSession):

    try:

        student_fetch_query = await db.execute(
                    select(Student).where(Student.stu_id == student_id)
        )
        student = student_fetch_query.scalar_one_or_none()
        if not student:
            return "Not found"

        db.delete(student)
        await db.commit

        return {"msg" : "Deleted Sucessfully"}

    except:
            import traceback
            traceback.print_exc()
            raise


from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

async def delete_student(student_id: int, db: AsyncSession):
    try:
        student_fetch_query = await db.execute(
            select(Student).where(Student.stu_id == student_id)
        )
        student = student_fetch_query.scalar_one_or_none()
 
        if not student:
            return {"error": "Not found"} 
        
        await db.delete(student)
        await db.commit()

        return {"msg": "Deleted Successfully"}

    except Exception as e:
        
        import traceback
        traceback.print_exc()
        raise



