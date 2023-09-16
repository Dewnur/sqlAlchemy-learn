from sqlalchemy.orm import Mapped, mapped_column

from app.models.base_model import BaseUUIDModel


class Faculty(BaseUUIDModel):
    __tablename__ = 'faculty'

    name: Mapped[str] = mapped_column(unique=True, nullable=False)