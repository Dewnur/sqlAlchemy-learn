from app.crud.crud_base import CRUDBase
from app.models.group_model import Group


class CRUDGroup(CRUDBase[Group]):
    pass


group = CRUDGroup(Group)
