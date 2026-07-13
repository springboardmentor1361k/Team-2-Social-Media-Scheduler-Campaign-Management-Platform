from pydantic import BaseModel


class PostCreate(BaseModel):
    campaign_id: int | None = None
    content_text: str
    status: str = "Draft"


class PostUpdate(BaseModel):
    campaign_id: int | None = None
    content_text: str
    status: str


class PostResponse(BaseModel):
    id: int
    campaign_id: int | None = None
    content_text: str
    status: str

    class Config:
        from_attributes = True