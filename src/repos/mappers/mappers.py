from src.repos.mappers.base import BaseMapper
from src.models.links import Links
from src.schemas.links import LinksView


class LinksDataMapper(BaseMapper):
    db_model = Links
    schema = LinksView