from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base_model import BaseUUIDModel

if TYPE_CHECKING:
    from subject_model import Subject
    from group_model import Group
    from teacher_model import Teacher


class Class(BaseUUIDModel):
    __tablename__ = "class"

    subject_id: Mapped[UUID] = mapped_column(ForeignKey('subject.id'), primary_key=True)
    group_id: Mapped[UUID] = mapped_column(ForeignKey('group.id'), primary_key=True)
    teacher_id: Mapped[UUID] = mapped_column(ForeignKey('teacher.id'), primary_key=True)

    subject: Mapped['Subject'] = relationship(back_populates='classes', lazy='selectin')
    group: Mapped['Group'] = relationship(back_populates='classes', lazy='selectin')
    teacher: Mapped['Teacher'] = relationship(back_populates='classes', lazy='selectin')
