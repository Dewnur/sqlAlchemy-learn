from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base_model import BaseUUIDModel
from app.models.profile_model import Profile

if TYPE_CHECKING:
    from group_model import Group
    from user_model import User


class Student(BaseUUIDModel, Profile):
    __tablename__ = "student"

    faculty: Mapped[str] = mapped_column()

    user: Mapped['User'] = relationship(back_populates='student', lazy='selectin')
    group: Mapped['Group'] = relationship(back_populates='students', lazy='selectin')
