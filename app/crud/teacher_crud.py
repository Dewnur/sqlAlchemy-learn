from app.crud.crud_base import CRUDBase
from app.models import Teacher


class CRUDTeacher(CRUDBase[Teacher]):
    pass


teacher = CRUDTeacher(Teacher)
