from fastapi import APIRouter, Body, Path, status
from fastapi.responses import RedirectResponse

from src.schemas.links import CreateLinksResponce, LinksAddRequest
from src.services.links import LinksServices
from src.api.dependencies import DBDep
from src.utils.exceptions import NotUniqueLinkException, LinkNotFoundException
from src.utils.http_exceptions import NotUniqueLinkHTTPException, LinkNotFoundHTTPException

router = APIRouter(tags=["Links"])


@router.post("/", response_model=CreateLinksResponce, status_code=201)
async def create_short_link(db: DBDep, dest_url_data: LinksAddRequest = Body()):
    try:
        data = await LinksServices(db).add(dest_url_data)
    except NotUniqueLinkException:
        raise NotUniqueLinkHTTPException
    return {"ok": True, "data": data}

@router.get("/{slug}", status_code=302)
async def get_dest_url(db: DBDep, slug: str = Path()):
    try:
        data = await LinksServices(db).get_dest_url(slug)
        print(data)
    except LinkNotFoundException:
        raise LinkNotFoundHTTPException
    print(data.dest_url)
    return RedirectResponse(
        url=data.dest_url,
        status_code=status.HTTP_302_FOUND
    )