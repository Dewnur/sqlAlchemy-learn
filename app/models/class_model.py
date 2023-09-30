from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base_model import BaseUUIDModel

if TYPE_CHECKING:
    from employee_model import Employee
    from student_model import Student


class Class(BaseUUIDModel):
    __tablename__ = "class"

    group_id: Mapped[UUID] = mapped_column()
    teacher_id: Mapped[UUID] = mapped_column()
