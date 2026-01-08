from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.pool.impl import NullPool
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from src.config import settings

engine = create_async_engine(url=settings.DB_URL)
session_maker = async_sessionmaker(bind=engine, expire_on_commit=False)

engine_null_pull = create_async_engine(url=settings.DB_URL, poolclass=NullPool)
session_maker_null_pool = async_sessionmaker(
    bind=engine_null_pull, expire_on_commit=False
)

class Base(DeclarativeBase):
    pass