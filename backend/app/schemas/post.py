from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class PostCreate(BaseModel):
    title: str
    content: str
    media_url: Optional[str] = None
    platform: str
    schedule_time: datetime

    is_draft: bool = False
    is_recurring: bool = False
    recurring_type: Optional[str] = None

    campaign_id: Optional[int] = None


class PostResponse(PostCreate):
    id: int
    status: str

    class Config:
        from_attributes = True