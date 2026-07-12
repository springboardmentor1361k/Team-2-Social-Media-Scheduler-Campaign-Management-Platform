from datetime import date
from models import SessionLocal, engine, Base, User, SocialAccount, Campaign, Post

def seed_database():
    # 1. Clear out old tables to ensure a fresh start
    print("Dropping old tables and recreating structures...")
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    
    db = SessionLocal()
    try:
        print("Seeding fresh authentication and platform data...")
        
        # 2. Add a test user with the new authentication columns
        test_user = User(
            full_name="Jay Rai",
            email="jay@example.com",
            username="jayrai123",
            hashed_password="fake_hashed_password_123", # Plain text placeholder for testing
            role="user",
            is_active=True
        )
        db.add(test_user)
        db.flush() # Flushes data to assign an ID to test_user before linking relationships
        
        # 3. Add a test Social Media Account linked to this user
        linked_account = SocialAccount(
            user_id=test_user.id,
            platform_name="LinkedIn",
            profile_name="jay-rai-dev"
        )
        db.add(linked_account)
        
        # 4. Add a test marketing campaign
        marketing_campaign = Campaign(
            user_id=test_user.id,
            campaign_name="Summer Internship Launch",
            start_date=date(2026, 7, 1),
            end_date=date(2026, 7, 31)
        )
        db.add(marketing_campaign)
        db.flush()
        
        # 5. Add a scheduled social media post
        sample_post = Post(
            user_id=test_user.id,
            campaign_id=marketing_campaign.id,
            content_text="Thrilled to kick off my backend engineering internship project!",
            status="Scheduled"
        )
        db.add(sample_post)
        
        # 6. Safely commit all changes to PostgreSQL
        db.commit()
        print("Database successfully seeded with updated structures!")
        
    except Exception as e:
        db.rollback()
        print(f"An error occurred during seeding: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    seed_database()