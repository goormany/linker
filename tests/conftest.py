from typing import AsyncGenerator
from httpx import ASGITransport, AsyncClient
import pytest

from src.api.dependencies import get_db
from src.main import app
from src.config import settings
from src.database import session_maker_null_pool, Base, engine_null_pull
from src.utils.db_manager import DBManager


@pytest.fixture(scope="session", autouse=True)
async def check_mode():
    assert settings.MODE == "TEST"

@pytest.fixture(scope="session", autouse=True)
async def setup_db(check_mode):
    async with engine_null_pull.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

async def get_db_null_pull():
    async with DBManager(session_maker_null_pool) as db:
        yield db

@pytest.fixture(scope="function")
async def db() -> AsyncGenerator[DBManager, None]:
    async for db in get_db_null_pull():
        yield db


app.dependency_overrides[get_db] = get_db_null_pull

@pytest.fixture(scope="session")
async def ac():
    async with AsyncClient(
        transport=ASGITransport(app=app), base_url="http://test"
    ) as ac:
        yield ac