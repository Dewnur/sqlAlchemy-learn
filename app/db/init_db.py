from sqlalchemy import insert, delete
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from app import crud
from app.db.data import DATA
from app.db.random_data import *
from app.models.faculty_model import Faculty
from app.models.user_model import User


async def init_db(async_session: async_sessionmaker[AsyncSession]) -> None:
    async with async_session() as session:
        length_employees = 50
        length_students = 950

        for f in DATA['faculty']:
            faculty = Faculty(
                id=uuid.uuid4(),
                name=f
            )
            await crud.faculty.create(faculty, db_session=async_session)
        for i in range(length_employees):
            user = get_random_user()
            await crud.user.create(user, db_session=async_session)
            employee = get_random_employee(user)
            await crud.employee.create(employee, db_session=async_session)
        for i in range(length_students):
            user = get_random_user()
            await crud.user.create(user, db_session=async_session)
            facultys = await crud.faculty.fetch_all(db_session=async_session)
            faculty = random.choice(facultys)
            student = get_random_student(user, faculty)
            await crud.student.create(student, db_session=async_session)


async def clear_db(async_session: async_sessionmaker[AsyncSession]) -> None:
    async with async_session() as session:
        models = [Faculty, Employee, Student, User]
        for m in models:
            await session.execute(delete(m))
        await session.commit()
