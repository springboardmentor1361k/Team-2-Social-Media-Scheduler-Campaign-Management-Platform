import os
import requests
from dotenv import load_dotenv

load_dotenv()


# =========================================================
# INSTAGRAM - REAL API INTEGRATION
# =========================================================

def publish_to_instagram(post):
    print(f"📸 Publishing '{post.title}' to Instagram...")

    access_token = os.getenv("INSTAGRAM_ACCESS_TOKEN")
    instagram_account_id = os.getenv("INSTAGRAM_ACCOUNT_ID")

    if not access_token:
        print("❌ Instagram access token not found.")
        return False

    if not instagram_account_id:
        print("❌ Instagram account ID not found.")
        return False

    media_url = getattr(post, "media_url", None)

    if not media_url:
        print("❌ No media URL found for this post.")
        return False

    caption = post.content or post.title

    try:

        # -------------------------------------------------
        # STEP 1: CREATE INSTAGRAM MEDIA CONTAINER
        # -------------------------------------------------

        create_url = (
            f"https://graph.instagram.com/"
            f"{instagram_account_id}/media"
        )

        create_data = {
            "image_url": media_url,
            "caption": caption,
            "access_token": access_token
        }

        response = requests.post(
            create_url,
            data=create_data,
            timeout=30
        )

        data = response.json()

        if response.status_code != 200 or "id" not in data:
            print("❌ Instagram media creation failed:")
            print(data)
            return False

        container_id = data["id"]

        print(
            f"✅ Media container created: "
            f"{container_id}"
        )

        # -------------------------------------------------
        # STEP 2: PUBLISH INSTAGRAM MEDIA CONTAINER
        # -------------------------------------------------

        publish_url = (
            f"https://graph.instagram.com/"
            f"{instagram_account_id}/media_publish"
        )

        publish_data = {
            "creation_id": container_id,
            "access_token": access_token
        }

        publish_response = requests.post(
            publish_url,
            data=publish_data,
            timeout=30
        )

        publish_data_response = publish_response.json()

        if (
            publish_response.status_code != 200
            or "id" not in publish_data_response
        ):
            print("❌ Instagram publishing failed:")
            print(publish_data_response)
            return False

        print(
            "✅ Instagram post published successfully!"
        )

        print(
            f"Instagram Media ID: "
            f"{publish_data_response['id']}"
        )

        return True

    except requests.RequestException as e:

        print(
            f"❌ Instagram API request failed: {e}"
        )

        return False

    except Exception as e:

        print(
            f"❌ Instagram publishing error: {e}"
        )

        return False


# =========================================================
# FACEBOOK - MOCK PUBLISHING
# =========================================================

def publish_to_facebook(post):

    print(
        f"📘 Publishing '{post.title}' "
        f"to Facebook..."
    )

    print(
        "🟡 Facebook publishing is running "
        "in MOCK mode."
    )

    print(
        "✅ Facebook mock publishing completed."
    )

    return {
        "success": True,
        "platform": "Facebook",
        "mode": "MOCK",
        "message":
            "Facebook post published successfully (Demo)"
    }


# =========================================================
# LINKEDIN - MOCK PUBLISHING
# =========================================================

def publish_to_linkedin(post):

    print(
        f"💼 Publishing '{post.title}' "
        f"to LinkedIn..."
    )

    print(
        "🟡 LinkedIn publishing is running "
        "in MOCK mode."
    )

    print(
        "✅ LinkedIn mock publishing completed."
    )

    return {
        "success": True,
        "platform": "LinkedIn",
        "mode": "MOCK",
        "message":
            "LinkedIn post published successfully (Demo)"
    }


# =========================================================
# TWITTER / X - MOCK PUBLISHING
# =========================================================

def publish_to_twitter(post):

    print(
        f"🐦 Publishing '{post.title}' "
        f"to X (Twitter)..."
    )

    print(
        "🟡 X/Twitter publishing is running "
        "in MOCK mode."
    )

    print(
        "✅ X/Twitter mock publishing completed."
    )

    return {
        "success": True,
        "platform": "Twitter/X",
        "mode": "MOCK",
        "message":
            "Twitter/X post published successfully (Demo)"
    }