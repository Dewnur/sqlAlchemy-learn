from typing import TypeVar, Generic, Tuple, Any, Sequence
from uuid import UUID

from sqlalchemy import select, text, Row
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from app.models.base_model import Base

ModelType = TypeVar("ModelType", bound=Base)


class CRUDBase(Generic[ModelType]):
    def __init__(self, model: type[ModelType]):
        self.model = model

    async def fetch_one(
            self, db_session: async_sessionmaker[AsyncSession] | None = None, **filter,
    ) -> ModelType | None:
        async with db_session() as session:
            query = select(self.model).filter_by(**filter)
            result = await session.execute(query)
            return result.fetchone()

    async def fetch_all(
            self, db_session: async_sessionmaker[AsyncSession] | None = None, **filter,
    ) -> Sequence[Row[tuple[Any, ...] | Any]]:
        async with db_session() as session:
            query = select(self.model).filter_by(**filter)
            result = await session.execute(query)
            return result.fetchall()

    async def create(self):
        pass

    async def update(self):
        pass

    async def delete(self):
        pass
