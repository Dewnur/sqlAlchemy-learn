import random
import uuid
from uuid import UUID

from faker import Faker

from app.models.employee_model import Employee
from app.models.faculty_model import Faculty
from app.models.student_model import Student
from app.models.user_model import User, Gender
from app.utils.random_string import random_string

fake = Faker(['ru_RU'])


def get_random_user() -> User:
    name = fake.name().split()
    return User(
        id=uuid.uuid4(),
        last_name=name[0],
        first_name=name[1],
        middle_name=name[2],
        age=random.randint(18, 50),
        gender=random.choice(list(Gender)),
        email=random_string() + fake.email(),
        phone_number=fake.phone_number()
    )


def get_random_employee(user: User) -> Employee:
    return Employee(
        user_id=user.id,
        salary=random.randint(40000, 100000),
        specialization='teacher',
        position=None
    )


def get_random_student(user: User, faculty: Faculty) -> Student:
    return Student(
        user_id=user.id,
        curse=1,
        faculty_id=faculty.id,
    )
