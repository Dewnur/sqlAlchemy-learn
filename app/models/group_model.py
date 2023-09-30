from typing import TYPE_CHECKING, List
from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base_model import BaseUUIDModel

if TYPE_CHECKING:
    from student_model import Student


class Group(BaseUUIDModel):
    __tablename__ = "group"

    student_id: Mapped[UUID] = mapped_column(ForeignKey('student.id'))
    students: Mapped[list['Student']] = relationship(
        back_populates='group', lazy='selectin')
