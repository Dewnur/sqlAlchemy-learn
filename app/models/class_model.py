from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base_model import BaseUUIDModel

if TYPE_CHECKING:
    from app.models import Group
    from app.models import Teacher


class Class(BaseUUIDModel):
    __tablename__ = "class"

    name: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column()

    teacher: Mapped['Teacher'] = relationship(secondary="class_teacher", backref='class')
    group: Mapped['Group'] = relationship(secondary="class_group", backref='class')
