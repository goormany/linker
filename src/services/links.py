from src.schemas.links import LinksAddRequest, LinksAdd
from src.services.base import BaseService
from src.utils.gen_slug import get_slug
from src.utils.exceptions import NotUniqueException, NotUniqueLinkException, ObjNotFoundException, LinkNotFoundException


class LinksServices(BaseService):
    async def add(self, dest_url_data: LinksAddRequest):
        new_data = LinksAdd(**dest_url_data.model_dump(), slug=get_slug())
        try:
            data = await self.db.links.add(new_data)
            await self.db.commit()
        except NotUniqueException as e:
            raise NotUniqueLinkException from e
        return data
    
    async def get_dest_url(self, slug: str):
        try:
            return await self.db.links.get_one(slug=slug)
        except ObjNotFoundException as e:
            raise LinkNotFoundException from e