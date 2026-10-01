from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column

from src.configs.model import Base


class Student(Base):
    __tablename__ = "students"

    stu_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)
    age: Mapped[int] = mapped_column(Integer)
    email: Mapped[str] = mapped_column(String)
    ph_no: Mapped[str] = mapped_column(String)