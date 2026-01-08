from pydantic import BaseModel, ConfigDict


class LinksAddRequest(BaseModel):
    dest_url: str


class LinksAdd(LinksAddRequest):
    slug: str


class LinksView(LinksAdd):
    id: int

    model_config = ConfigDict(from_attributes=True)


class CreateLinksResponce(BaseModel):
    ok: bool = True
    data: LinksView

    model_config = ConfigDict(from_attributes=True)
