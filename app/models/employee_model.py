from typing import List
from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base_model import BaseUUIDModel
from app.models.discipline_model import Discipline
from app.models.profile_model import Profile


class Employee(BaseUUIDModel, Profile):
    __tablename__ = "employee"

    salary: Mapped[int] = mapped_column()
    specialization: Mapped[str] = mapped_column(nullable=True)
    position: Mapped[str] = mapped_column(nullable=True)
    disciplines: Mapped[List[Discipline]] = relationship("Discipline")
