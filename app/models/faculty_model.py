from typing import List

from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base_model import BaseUUIDModel
from app.models.student_model import Student


class Faculty(BaseUUIDModel):
    __tablename__ = 'faculty'

    name: Mapped[str] = mapped_column(unique=True, nullable=False)
    student: Mapped['Student'] = relationship("Student")