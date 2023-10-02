from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from app import crud
from app.db.data import DATA
from app.db.random_data import get_random_user, get_random_employee, get_random_student, get_random_teacher
from app.models import Base
from app.utils.array_functions import chunkify
from app.utils.timer import async_timer


@async_timer
async def init_db(async_session: async_sessionmaker[AsyncSession]) -> None:
    length_employees = 200
    length_students = 2000

    for i in range(length_employees):
        user = get_random_user()
        await crud.user.create(user, db_session=async_session)
        employee = get_random_employee(user)
        await crud.employee.create(employee, db_session=async_session)

    for i in range(length_students):
        user = get_random_user()
        await crud.user.create(user, db_session=async_session)
        student = get_random_student(user)
        await crud.student.create(student, db_session=async_session)

    teachers = await crud.employee.fetch_all(position='Teacher', db_session=async_session)
    for t in teachers:
        teacher = get_random_teacher(t)
        await crud.teacher.create(teacher, db_session=async_session)

    max_in_group = 30
    for faculty in DATA['faculties']:
        students = await crud.student.fetch_all(faculty=faculty, db_session=async_session)
        if not len(students):
            continue
        chunk_list = chunkify(len(students), max_in_group)
        groups = []
        prev = 0
        for ch in chunk_list:
            groups.append(students[prev:prev + ch])
            prev = prev + ch
        for i, group in enumerate(groups, 1):
            await crud.group.create_many(name=f'[{faculty}]-{i}', students=groups, db_session=async_session)

    print('Random data created')


async def clear_db(async_session: async_sessionmaker[AsyncSession]) -> None:
    async with async_session() as session:
        for tbl in reversed(Base.metadata.sorted_tables):
            await session.execute(tbl.delete())
        await session.commit()

    print('Database is clear')
