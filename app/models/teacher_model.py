from typing import TYPE_CHECKING, List
from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base_model import BaseUUIDModel

if TYPE_CHECKING:
    from employee_model import Employee
    from class_model import Class


class Teacher(BaseUUIDModel):
    __tablename__ = "teacher"

    employee_id: Mapped[UUID] = mapped_column(ForeignKey('employee.id'))

    employee: Mapped['Employee'] = relationship(back_populates='teacher', lazy='selectin')
    classes: Mapped[List['Class']] = relationship(back_populates='teacher')
