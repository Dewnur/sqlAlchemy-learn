from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base_model import BaseUUIDModel

if TYPE_CHECKING:
    from class_model import Class


class Subject(BaseUUIDModel):
    __tablename__ = "subject"

    name: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column()

    classes: Mapped['Class'] = relationship(back_populates='subject')
