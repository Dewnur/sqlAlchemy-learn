from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base_model import BaseUUIDModel


class ClassGroup(BaseUUIDModel):
    __tablename__ = "class_group"

    class_id: Mapped[UUID] = mapped_column(ForeignKey('class.id'), primary_key=True)
    group_id: Mapped[UUID] = mapped_column(ForeignKey('group.id'), primary_key=True)
