from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.campaign import Campaign
from app.models.user import User
from app.schemas.campaign import (
    CampaignCreate,
    CampaignUpdate,
    CampaignResponse,
)
from app.core.dependencies import get_current_user

router = APIRouter(
    prefix="/campaigns",
    tags=["Campaigns"],
)


@router.post("/", response_model=CampaignResponse)
def create_campaign(
    campaign: CampaignCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    new_campaign = Campaign(
        campaign_name=campaign.campaign_name,
        start_date=campaign.start_date,
        end_date=campaign.end_date,
        user_id=current_user.id,
    )

    db.add(new_campaign)
    db.commit()
    db.refresh(new_campaign)

    return new_campaign


@router.get("/", response_model=list[CampaignResponse])
def get_campaigns(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    return (
        db.query(Campaign)
        .filter(Campaign.user_id == current_user.id)
        .all()
    )


@router.get("/{campaign_id}", response_model=CampaignResponse)
def get_campaign(
    campaign_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    campaign = (
        db.query(Campaign)
        .filter(
            Campaign.id == campaign_id,
            Campaign.user_id == current_user.id,
        )
        .first()
    )

    if not campaign:
        raise HTTPException(404, "Campaign not found")

    return campaign


@router.put("/{campaign_id}", response_model=CampaignResponse)
def update_campaign(
    campaign_id: int,
    campaign_data: CampaignUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    campaign = (
        db.query(Campaign)
        .filter(
            Campaign.id == campaign_id,
            Campaign.user_id == current_user.id,
        )
        .first()
    )

    if not campaign:
        raise HTTPException(404, "Campaign not found")

    campaign.campaign_name = campaign_data.campaign_name
    campaign.start_date = campaign_data.start_date
    campaign.end_date = campaign_data.end_date

    db.commit()
    db.refresh(campaign)

    return campaign


@router.delete("/{campaign_id}")
def delete_campaign(
    campaign_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    campaign = (
        db.query(Campaign)
        .filter(
            Campaign.id == campaign_id,
            Campaign.user_id == current_user.id,
        )
        .first()
    )

    if not campaign:
        raise HTTPException(404, "Campaign not found")

    db.delete(campaign)
    db.commit()

    return {
        "message": "Campaign deleted successfully"
    }