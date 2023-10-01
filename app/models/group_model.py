from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base_model import BaseUUIDModel

if TYPE_CHECKING:
    from student_model import Student
    from class_model import Class


class Group(BaseUUIDModel):
    __tablename__ = "group"

    name: Mapped[str] = mapped_column()
    student_id: Mapped[UUID] = mapped_column(ForeignKey('student.id'))

    students: Mapped[list['Student']] = relationship(
        back_populates='group', lazy='selectin')
    classes: Mapped['Class'] = relationship(back_populates='group')
