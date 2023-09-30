from sqlalchemy import delete
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from app import crud
from app.db.random_data import get_random_user, get_random_employee, get_random_student
from app.models.employee_model import Employee
from app.models.student_model import Student
from app.models.teacher_model import Teacher
from app.models.user_model import User
from app.utils.timer import async_timer

MODELS_LIST = [Teacher, Student, Employee, User]


@async_timer
async def init_db(async_session: async_sessionmaker[AsyncSession]) -> None:
    length_employees = 50
    length_students = 950

    await clear_db(async_session)

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


async def clear_db(async_session: async_sessionmaker[AsyncSession]) -> None:
    async with async_session() as session:
        for m in [Teacher, Student, Employee, User]:
            await session.execute(delete(m))
        await session.commit()
