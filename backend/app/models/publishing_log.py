from sqlalchemy import Column, Integer, String, DateTime
from database import Base
from datetime import datetime


class PublishingLog(Base):
    __tablename__ = "publishing_logs"

    id = Column(Integer, primary_key=True, index=True)
    post_id = Column(Integer, nullable=False)
    post_title = Column(String, nullable=False)
    platform = Column(String, nullable=False)
    status = Column(String, nullable=False)
    published_at = Column(DateTime, default=datetime.utcnow)
    message = Column(String, nullable=True)