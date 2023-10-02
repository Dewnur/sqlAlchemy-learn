import random
import uuid

from faker import Faker

from app.db.data import DATA
from app.models import User, Gender, Employee, Student, Teacher
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
        position=random.choice(DATA['positions'])
    )


def get_random_student(user: User) -> Student:
    return Student(
        user_id=user.id,
        faculty=random.choice(DATA['faculties'])
    )


def get_random_teacher(employee: Employee) -> Teacher:
    return Teacher(
        employee_id=employee.id,
    )

