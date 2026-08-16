from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from models.campaign import Campaign

router = APIRouter()


# ==========================
# ENGAGEMENT ANALYTICS
# ==========================
@router.get("/campaign/{id}/analytics")
def campaign_analytics(id: int, db: Session = Depends(get_db)):
    campaign = db.query(Campaign).filter(Campaign.id == id).first()

    if not campaign:
        return {"error": "Campaign not found"}

    # Dummy analytics (Facebook API integration taruvata real values)
    likes = 250
    comments = 80
    shares = 45
    reach = 3000

    engagement_rate = round(
        ((likes + comments + shares) / reach) * 100,
        2
    )

    return {
        "campaign_id": campaign.id,
        "campaign_name": campaign.campaign_name,
        "likes": likes,
        "comments": comments,
        "shares": shares,
        "reach": reach,
        "engagement_rate": f"{engagement_rate}%"
    }


# ==========================
# ROI CALCULATION
# ==========================
@router.get("/campaign/{id}/roi")
def campaign_roi(id: int, db: Session = Depends(get_db)):
    campaign = db.query(Campaign).filter(Campaign.id == id).first()

    if not campaign:
        return {"error": "Campaign not found"}

    revenue = 12000.0
    budget = campaign.budget or 1

    roi = ((revenue - budget) / budget) * 100

    return {
        "campaign_id": campaign.id,
        "campaign_name": campaign.campaign_name,
        "budget": budget,
        "revenue": revenue,
        "roi_percentage": round(roi, 2)
    }


# ==========================
# CAMPAIGN COMPARISON
# ==========================
@router.get("/campaign/compare")
def compare_campaigns(db: Session = Depends(get_db)):
    campaigns = db.query(Campaign).all()

    comparison = []

    for campaign in campaigns:
        comparison.append({
            "campaign_id": campaign.id,
            "campaign_name": campaign.campaign_name,
            "platform": campaign.platform,
            "budget": campaign.budget,
            "status": campaign.status
        })

    return {
        "total_campaigns": len(comparison),
        "campaigns": comparison
    }