from typing import TypeVar

from pydantic import BaseModel

from src.database import Base

DBModelType = TypeVar("Base", bound=Base)
SchemaType = TypeVar("BaseModel", bound=BaseModel)


class BaseMapper:
    db_model: type[DBModelType] = None
    schema: type[SchemaType] = None

    @classmethod
    def map_to_schema(cls, data: Base) -> BaseModel:
        return cls.schema.model_validate(data, from_attributes=True)

    @classmethod
    def map_to_db_model(cls, data: BaseModel) -> Base:
        return cls.db_model(**data.model_dump())
