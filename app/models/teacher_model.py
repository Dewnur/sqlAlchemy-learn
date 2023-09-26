from uuid import UUID

from sqlalchemy.orm import mapped_column, Mapped

from app.models.base_model import BaseUUIDModel


class Teacher(BaseUUIDModel):
    __tablename__ = "teacher"

    faculty_id : Mapped[UUID] = mapped_column()
    employee_id : Mapped[UUID] = mapped_column()


