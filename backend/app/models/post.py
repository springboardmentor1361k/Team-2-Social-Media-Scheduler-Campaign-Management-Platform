from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from database import Base


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    media_url = Column(String, nullable=True)
    platform = Column(String, nullable=False)

    schedule_time = Column(DateTime)

    status = Column(String, default="Pending")

    # New Fields
    is_draft = Column(Boolean, default=False)
    is_recurring = Column(Boolean, default=False)
    recurring_type = Column(String, nullable=True)   # daily / weekly / monthly
    published_at = Column(DateTime, nullable=True)

    campaign_id = Column(Integer, ForeignKey("campaigns.id"))
    campaign = relationship("Campaign", back_populates="posts")