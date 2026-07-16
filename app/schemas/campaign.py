from datetime import date
from pydantic import BaseModel


class CampaignCreate(BaseModel):
    campaign_name: str
    start_date: date | None = None
    end_date: date | None = None


class CampaignUpdate(BaseModel):
    campaign_name: str
    start_date: date | None = None
    end_date: date | None = None


class CampaignResponse(BaseModel):
    id: int
    campaign_name: str
    start_date: date | None
    end_date: date | None

    model_config = {
        "from_attributes": True
    }