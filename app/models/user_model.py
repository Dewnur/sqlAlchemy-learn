from enum import Enum
from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base_model import BaseUUIDModel

if TYPE_CHECKING:
    from app.models.student_model import Student
    from app.models.employee_model import Employee


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
    phone_number: Mapped[str] = mapped_column(nullable=True)

    student: Mapped['Student'] = relationship(back_populates='user', lazy='selectin')
    employee: Mapped['Employee'] = relationship(back_populates='user', lazy='selectin')
