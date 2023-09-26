from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base_model import BaseUUIDModel
from app.models.profile_model import Profile


class Student(BaseUUIDModel, Profile):
    __tablename__ = "student"

    curse: Mapped[int] = mapped_column()
    faculty_id: Mapped[UUID] = mapped_column(ForeignKey('faculty.id'))
