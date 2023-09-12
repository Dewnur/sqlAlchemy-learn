import asyncio

from sqlalchemy import insert
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession

from app.datebase import async_session
from app.models.student_model import Student
from app.models.user_model import Gender


async def insert_student(
        async_session: async_sessionmaker[AsyncSession],
) -> None:
    async with async_session() as session:
        stmt = insert(Student).values(name="Jane", age=22, gender=Gender.female)
        await session.execute(stmt)
        await session.commit()
        return


async def async_main() -> None:
    await insert_student(async_session)


if __name__ == '__main__':
    asyncio.run(async_main())
