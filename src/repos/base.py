from pydantic import BaseModel
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError, NoResultFound
from asyncpg.exceptions import UniqueViolationError

from src.database import Base
from src.repos.mappers.base import BaseMapper
from src.utils.exceptions import NotUniqueException, ObjNotFoundException


class BaseRepository:
    model: Base = None
    mapper: BaseMapper = None
    
    def __init__(self, session: AsyncSession):
        self.session = session
    
    async def get_one(self, *args, **kwargs):
        query = (
            select(self.model)
            .filter(*args)
            .filter_by(**kwargs)
        )
        res = await self.session.execute(query)
        try:
            res = res.scalar_one()
        except NoResultFound as e:
            raise ObjNotFoundException from e

        return self.mapper.map_to_schema(res)
    
    async def get_all(self):
        return await self.get_filtred()
    
    async def add(self, data: BaseModel, exclude_unset: bool = False):
        add_stmt = (
            insert(self.model)
            .values(**data.model_dump(exclude_unset=exclude_unset))
            .returning(self.model)
        )
        try:
            res = await self.session.execute(add_stmt)
        except IntegrityError as e:
            if isinstance(e.orig.__cause__, UniqueViolationError):
                raise NotUniqueException from e
            else:
                raise e
        return self.mapper.map_to_schema(res.scalar_one())