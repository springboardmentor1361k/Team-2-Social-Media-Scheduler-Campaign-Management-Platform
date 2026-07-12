from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Date, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

# 1. Database Configuration Setup
# Replace with your actual local database credentials
DATABASE_URL = "postgresql+psycopg2://postgres:123456@localhost:5432/social_scheduler"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# ==========================================
# 2. DATABASE CORE TABLES
# ==========================================

class User(Base):
    __tablename__ = "users"

    # Core Columns & Authentication Fields
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    username = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(String, default="user")           # e.g., 'admin', 'user'
    is_active = Column(Boolean, default=True)

    # Relationships to other tables
    social_accounts = relationship("SocialAccount", back_populates="user", cascade="all, delete-orphan")
    campaigns = relationship("Campaign", back_populates="user", cascade="all, delete-orphan")
    posts = relationship("Post", back_populates="user", cascade="all, delete-orphan")


class SocialAccount(Base):
    __tablename__ = "social_accounts"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    platform_name = Column(String, nullable=False)  # e.g., 'LinkedIn', 'Twitter'
    profile_name = Column(String, nullable=False)   # Handle or username on that platform

    # Relationship back to User
    user = relationship("User", back_populates="social_accounts")


class Campaign(Base):
    __tablename__ = "campaigns"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    campaign_name = Column(String, nullable=False)
    start_date = Column(Date, nullable=True)
    end_date = Column(Date, nullable=True)

    # Relationships
    user = relationship("User", back_populates="campaigns")
    posts = relationship("Post", back_populates="campaign")


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    campaign_id = Column(Integer, ForeignKey("campaigns.id", ondelete="SET NULL"), nullable=True)
    content_text = Column(Text, nullable=False)
    status = Column(String, default="Draft")        # e.g., 'Draft', 'Scheduled', 'Published'

    # Relationships back to parents
    user = relationship("User", back_populates="posts")
    campaign = relationship("Campaign", back_populates="posts")


# ==========================================
# 3. COMPILATION INITIATOR
# ==========================================
def init_db():
    """Compiles and builds all structure blueprints directly onto the live PostgreSQL server instance."""
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    print("Initializing database tables...")
    init_db()
    print("Database tables created successfully!")