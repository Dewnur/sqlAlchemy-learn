from sqlalchemy import insert, delete
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from app import crud
from app.db.data import FACULTY
from app.db.random_data import *
from app.models.faculty_model import Faculty
from app.models.user_model import User


async def init_db(async_session: async_sessionmaker[AsyncSession]) -> None:
    async with async_session() as session:
        length_employees = 50
        length_students = 950

        for f in FACULTY:
            stmt = insert(Faculty).values(name=f)
            await session.execute(stmt)
        for i in range(length_employees):
            user = get_random_user()
            await crud.user.create(user, db_session=async_session)
            employee = get_random_employee(user)
            await crud.employee.create(employee, db_session=async_session)
        for i in range(length_students):
            user = get_random_user()
            await crud.user.create(user, db_session=async_session)
            employee = get_random_employee(user)
            await crud.employee.create(employee, db_session=async_session)

async def clear_db(async_session: async_sessionmaker[AsyncSession]) -> None:
    async with async_session() as session:
        models = [User, Faculty, Employee]
        for m in models:
            await session.execute(delete(m))
        await session.commit()
