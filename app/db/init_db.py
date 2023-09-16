from typing import List

from sqlalchemy import insert, delete
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from app.db.data import FACULTY
from app.db.random_data import *
from app.models.faculty_model import Faculty
from app.models.user_model import User


async def init_db(async_session: async_sessionmaker[AsyncSession]) -> None:
    async with async_session() as session:
        length_users = 1000
        length_employees = 50
        length_students = 950
        users: List[User] = [get_random_user() for i in range(length_users)]

        for f in FACULTY:
            stmt = insert(Faculty).values(name=f)
            await session.execute(stmt)
        for u in users:
            session.add(u)
        await session.commit()


async def clear_db(async_session: async_sessionmaker[AsyncSession]) -> None:
    async with async_session() as session:
        models = [User, Faculty]
        for m in models:
            await session.execute(delete(m))
        await session.commit()
