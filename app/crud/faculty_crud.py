from app.crud.crud_base import CRUDBase
from app.models.faculty_model import Faculty


class CRUDFaculty(CRUDBase[Faculty]):
    pass


faculty = CRUDFaculty(Faculty)