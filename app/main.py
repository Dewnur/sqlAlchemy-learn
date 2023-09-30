import asyncio

from app.db.init_db import init_db
from app.db.session import async_session


async def async_main() -> None:
    await init_db(async_session) if True else None


if __name__ == '__main__':
    asyncio.run(async_main())
