from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base_model import BaseUUIDModel


class ClassTeacher(BaseUUIDModel):
    __tablename__ = "class_teacher"

    class_id: Mapped[UUID] = mapped_column(ForeignKey('class.id'), primary_key=True)
    teacher_id: Mapped[UUID] = mapped_column(ForeignKey('teacher.id'), primary_key=True)
