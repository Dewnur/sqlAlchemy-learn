from enum import Enum
from typing import List

from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base_model import BaseUUIDModel
from app.models.employee_model import Employee
from app.models.student_model import Student


class Gender(str, Enum):
    female = "female"
    male = "male"
    other = "other"


class User(BaseUUIDModel):
    __tablename__ = "user"

    first_name: Mapped[str] = mapped_column()
    last_name: Mapped[str] = mapped_column()
    middle_name: Mapped[str] = mapped_column(nullable=True)
    age: Mapped[int] = mapped_column(nullable=True)
    gender: Mapped[Gender] = mapped_column(default=Gender.other)
    email: Mapped[str] = mapped_column(nullable=True, unique=True)
    bio: Mapped[str] = mapped_column(nullable=True)
    phone_number: Mapped[str] = mapped_column(nullable=True)
    employees: Mapped[List[Employee]] = relationship("Employee")
    students: Mapped[List[Student]] = relationship("Student")

