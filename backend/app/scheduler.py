from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime, timedelta
from sqlalchemy.orm import Session

from database import SessionLocal
from models.post import Post
from models.notification import Notification
from models.publishing_log import PublishingLog

from services.social_media import (
    publish_to_instagram,
    publish_to_facebook,
    publish_to_linkedin,
    publish_to_twitter,
)

scheduler = BackgroundScheduler()


def publish_posts():

    db: Session = SessionLocal()

    try:

        # ==========================================
        # GET PENDING NON-DRAFT POSTS
        # ==========================================

        posts = (
            db.query(Post)
            .filter(
                Post.status == "Pending",
                Post.is_draft == False
            )
            .all()
        )

        print(f"Found {len(posts)} pending post(s)")

        current_time = datetime.now()

        for post in posts:

            if post.schedule_time is None:
                continue

            if post.schedule_time <= current_time:

                print(f"Publishing: {post.title}")

                # ==========================================
                # MARK AS PUBLISHING
                # ==========================================

                post.status = "Publishing"
                db.commit()

                publish_success = False

                # ==========================================
                # SOCIAL MEDIA PUBLISHING
                # ==========================================

                try:

                    if post.platform == "Instagram":

                        publish_success = publish_to_instagram(post)

                    elif post.platform == "Facebook":

                        result = publish_to_facebook(post)

                        publish_success = (
                            result.get("success", False)
                            if isinstance(result, dict)
                            else bool(result)
                        )

                    elif post.platform == "LinkedIn":

                        result = publish_to_linkedin(post)

                        publish_success = (
                            result.get("success", False)
                            if isinstance(result, dict)
                            else bool(result)
                        )

                    elif post.platform == "Twitter":

                        result = publish_to_twitter(post)

                        publish_success = (
                            result.get("success", False)
                            if isinstance(result, dict)
                            else bool(result)
                        )

                    else:

                        print(
                            f"❌ Platform '{post.platform}' "
                            f"is not supported."
                        )

                except Exception as e:

                    print(
                        f"❌ Publishing exception for "
                        f"{post.title}: {e}"
                    )

                    publish_success = False

                # ==========================================
                # SUCCESS
                # ==========================================

                if publish_success:

                    post.status = "Published"
                    post.published_at = datetime.now()

                    log = PublishingLog(
                        post_id=post.id,
                        post_title=post.title,
                        platform=post.platform,
                        status="Published",
                        published_at=datetime.now(),
                        message=(
                            f"{post.title} published successfully "
                            f"on {post.platform}"
                        )
                    )

                    db.add(log)

                    notification = Notification(
                        message=(
                            f"{post.title} published successfully "
                            f"on {post.platform}"
                        )
                    )

                    db.add(notification)

                    print(
                        f"✅ {post.title} published successfully "
                        f"on {post.platform}"
                    )

                    # ==========================================
                    # RECURRING POST
                    # ==========================================

                    if post.is_recurring:

                        next_schedule = post.schedule_time

                        if post.recurring_type == "daily":

                            next_schedule += timedelta(days=1)

                        elif post.recurring_type == "weekly":

                            next_schedule += timedelta(days=7)

                        elif post.recurring_type == "monthly":

                            next_schedule += timedelta(days=30)

                        new_post = Post(
                            title=post.title,
                            content=post.content,
                            media_url=post.media_url,
                            platform=post.platform,
                            schedule_time=next_schedule,
                            status="Pending",
                            is_draft=False,
                            is_recurring=True,
                            recurring_type=post.recurring_type,
                            campaign_id=post.campaign_id
                        )

                        db.add(new_post)

                        print(
                            f"🔁 Recurring post created for "
                            f"{next_schedule}"
                        )

                # ==========================================
                # FAILURE
                # ==========================================

                else:

                    post.status = "Failed"

                    log = PublishingLog(
                        post_id=post.id,
                        post_title=post.title,
                        platform=post.platform,
                        status="Failed",
                        published_at=datetime.now(),
                        message=(
                            f"{post.title} failed to publish "
                            f"on {post.platform}"
                        )
                    )

                    db.add(log)

                    print(
                        f"❌ Publishing failed: "
                        f"{post.title}"
                    )

        db.commit()

    except Exception as e:

        print(f"❌ Scheduler error: {e}")

        db.rollback()

    finally:

        db.close()


def start_scheduler():

    scheduler.add_job(
        publish_posts,
        "interval",
        seconds=10,
        max_instances=1,
        coalesce=True
    )

    scheduler.start()

    print("Scheduler Started Successfully!")
    