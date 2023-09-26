from typing import TypeVar, Generic, List

from sqlalchemy import select, insert, update, delete
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
            result = result.fetchone()
            return result[0] if result else None

    async def fetch_all(
            self, db_session: async_sessionmaker[AsyncSession] | None = None, **filter,
    ) -> List[ModelType] | None:
        async with db_session() as session:
            query = select(self.model).filter_by(**filter)
            result = await session.execute(query)
            result = result.fetchall()
            return [row[0] for row in result] if result else None

    async def create(
            self, model: ModelType, db_session: async_sessionmaker[AsyncSession] | None = None,
    ) -> None:
        async with db_session() as session:
            data = model.__dict__.copy()
            data.pop('_sa_instance_state')
            stmt = insert(self.model).values(**data)
            await session.execute(stmt)
            await session.commit()

    async def update(
            self, model: ModelType, db_session: async_sessionmaker[AsyncSession] | None = None, **param
    ) -> None:
        async with db_session() as session:
            data = model.__dict__.copy()
            data.pop('_sa_instance_state')
            stmt = update(self.model).filter_by(id=data['id']).values(**param)
            await session.execute(stmt)
            await session.commit()

    async def delete(
            self, model: ModelType, db_session: async_sessionmaker[AsyncSession] | None = None
    ) -> None:
        async with db_session() as session:
            data = model.__dict__.copy()
            data.pop('_sa_instance_state')
            stmt = delete(self.model).filter_by(id=data['id'])
            await session.execute(stmt)
            await session.commit()
