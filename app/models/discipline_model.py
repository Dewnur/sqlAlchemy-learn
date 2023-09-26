from sqlalchemy.orm import Mapped, mapped_column

from app.models.base_model import BaseUUIDModel


class Discipline(BaseUUIDModel):
    __tablename__ = "discipline"

    name: Mapped[str] = mapped_column(unique=True, nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)
