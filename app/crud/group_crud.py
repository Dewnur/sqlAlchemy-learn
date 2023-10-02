from typing import List

from sqlalchemy import insert
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession

from app.crud.crud_base import CRUDBase
from app.models import Student
from app.models.group_model import Group


class CRUDGroup(CRUDBase[Group]):
    async def create_many(
            self,
            name: str,
            students: List[Student],
            db_session: async_sessionmaker[AsyncSession] | None = None,
    ) -> None:
        async with db_session() as session:
            for student in students:
                stmt = insert(self.model).values(student_id=student.id, name=name)
                await session.execute(stmt)
                await session.commit()


group = CRUDGroup(Group)
