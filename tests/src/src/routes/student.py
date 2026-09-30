from fastapi import APIRouter

from src.modules.student.routes import student_router

# Configured Router for User Routes
root_user_router = APIRouter(prefix="/stu")

# Include User Auth Routers
root_user_router.include_router(student_router, tags=["Student Routes"])
