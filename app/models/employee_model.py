from sqlalchemy.orm import Mapped, mapped_column

from app.models.base_model import BaseUUIDModel
from app.models.profile_model import Profile


class Employee(BaseUUIDModel, Profile):
    __tablename__ = "employee"

    salary: Mapped[int] = mapped_column()
    specialization: Mapped[str] = mapped_column()
    position: Mapped[str] = mapped_column()
