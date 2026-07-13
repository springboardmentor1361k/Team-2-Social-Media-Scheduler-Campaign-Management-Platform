from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship

from app.db.database import Base


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(
        Integer,
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False
    )
    campaign_id = Column(
        Integer,
        ForeignKey("campaigns.id", ondelete="SET NULL"),
        nullable=True
    )
    content_text = Column(Text, nullable=False)
    status = Column(String, default="Draft")

    user = relationship("User", back_populates="posts")
    campaign = relationship("Campaign", back_populates="posts")