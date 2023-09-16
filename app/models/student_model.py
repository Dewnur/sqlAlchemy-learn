from typing import List

from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base_model import BaseUUIDModel
from app.models.discipline_model import Discipline
from app.models.profile_model import Profile


class Student(BaseUUIDModel, Profile):
    __tablename__ = "student"

    curse: Mapped[int] = mapped_column()
    faculty: Mapped[str] = mapped_column()
    disciplines: Mapped[List[Discipline]] = relationship("Discipline")
