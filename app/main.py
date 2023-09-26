import asyncio

from app import crud
from app.db.init_db import init_db, clear_db
from app.db.session import async_session


async def async_main() -> None:
    init = 0
    if init:
        await clear_db(async_session)
        await init_db(async_session)
    # user_obj = User(first_name='Имя', last_name='Фамилия', age=25)
    # await crud.user.create(user_obj, db_session=async_session)
    # user_obj = await crud.user.fetch_one(first_name='Имя', db_session=async_session)
    # await crud.user.update(user_obj, first_name='ИмяUpdate', db_session=async_session)
    # await crud.user.delete(user_obj, db_session=async_session)
    faculty = await crud.faculty.fetch_one(db_session=async_session)
    students = await crud.student.fetch_all(faculty_id=faculty.id,db_session=async_session)
    print(students)


if __name__ == '__main__':
    asyncio.run(async_main())
