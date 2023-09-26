from app.crud.crud_base import CRUDBase
from app.models.student_model import Student


class CRUDStudent(CRUDBase[Student]):
    pass


student = CRUDStudent(Student)