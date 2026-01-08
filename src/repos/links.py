from src.repos.base import BaseRepository
from src.repos.mappers.mappers import LinksDataMapper
from src.models.links import Links


class LinksRepository(BaseRepository):
    model = Links
    mapper = LinksDataMapper
