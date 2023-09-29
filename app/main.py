import asyncio

from app.db.init_db import init_db
from app.db.session import async_session, mongo_client as client


async def async_main() -> None:
    await init_db(async_session) if False else None
    db = client.database

    faculties = [f async for f in db.faculties.find({}, {'_id': 0})]
    print(faculties)


if __name__ == '__main__':
    asyncio.run(async_main())
