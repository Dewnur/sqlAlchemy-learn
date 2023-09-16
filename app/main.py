import asyncio
from uuid import UUID

from app import crud
from app.db.init_db import init_db, clear_db
from app.db.session import async_session


async def async_main() -> None:
    # await clear_db(async_session)
    # await init_db(async_session)
    obj = await crud.user.fetch_all(age=25, db_session=async_session)
    print(len(obj))
    print(obj)


if __name__ == '__main__':
    asyncio.run(async_main())
