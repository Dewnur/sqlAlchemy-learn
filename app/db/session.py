from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from app.config import DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME, MONGO_DB_USER, MONGO_DB_PASS

DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

MONGO_URL = f"mongodb://{MONGO_DB_USER}:{MONGO_DB_PASS}@localhost:27017/?authMechanism=DEFAULT"

engine = create_async_engine(DATABASE_URL)
async_session = async_sessionmaker(engine, expire_on_commit=False)

mongo_client = AsyncIOMotorClient(MONGO_URL, server_api=ServerApi('1'))

