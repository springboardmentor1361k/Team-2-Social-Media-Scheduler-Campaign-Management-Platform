from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from models.publishing_log import PublishingLog

router = APIRouter(prefix="/logs", tags=["Publishing Logs"])


@router.get("/")
def get_publishing_logs(db: Session = Depends(get_db)):
    logs = db.query(PublishingLog).order_by(
        PublishingLog.published_at.desc()
    ).all()

    return {
        "total_logs": len(logs),
        "logs": logs
    }