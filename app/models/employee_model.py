from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base_model import BaseUUIDModel
from app.models.profile_model import Profile

if TYPE_CHECKING:
    from user_model import User
    from teacher_model import Teacher


class Employee(BaseUUIDModel, Profile):
    __tablename__ = "employee"

    salary: Mapped[int] = mapped_column()
    position: Mapped[str] = mapped_column(nullable=True)

    user: Mapped['User'] = relationship(back_populates='employee', lazy='selectin')
