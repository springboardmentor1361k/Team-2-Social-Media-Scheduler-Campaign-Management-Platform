from fastapi import FastAPI

from app.db.database import Base, engine

# Import all models
from app.models import User, SocialAccount, Campaign, Post

# Import API routers
from app.api.auth import router as auth_router
from app.api.social_account import router as social_account_router
from app.api.campaign import router as campaign_router
from app.api.post import router as post_router

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="SocialPilot Backend API",
    version="1.0.0"
)

# Register API routers
app.include_router(auth_router)
app.include_router(social_account_router)
app.include_router(campaign_router)
app.include_router(post_router)


@app.get("/")
def root():
    return {
        "message": "Welcome to SocialPilot Backend API"
    }