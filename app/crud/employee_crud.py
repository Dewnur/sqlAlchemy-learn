from app.crud.crud_base import CRUDBase
from app.models.employee_model import Employee


class CRUDEmployee(CRUDBase[Employee]):
    pass


employee = CRUDEmployee(Employee)
