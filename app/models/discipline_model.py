from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base_model import BaseUUIDModel


class Discipline(BaseUUIDModel):
    __tablename__ = "discipline"

    name: Mapped[str] = mapped_column(unique=True, nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)
    employee_id: Mapped[UUID] = mapped_column(ForeignKey("employee.id"))
    student_id: Mapped[UUID] = mapped_column(ForeignKey("student.id"))
