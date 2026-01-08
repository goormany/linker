from typing import Annotated

from fastapi import Depends

from src.database import session_maker
from src.utils.db_manager import DBManager


async def get_db():
    async with DBManager(session_factory=session_maker) as db:
        yield db


DBDep = Annotated[DBManager, Depends(get_db)]
