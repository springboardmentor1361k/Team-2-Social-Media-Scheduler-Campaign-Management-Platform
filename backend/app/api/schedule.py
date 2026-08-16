from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database import get_db
from models.post import Post
from schemas.post import PostCreate

router = APIRouter()


# CREATE
@router.post("/schedule")
def create_schedule(post: PostCreate, db: Session = Depends(get_db)):
    new_post = Post(
        title=post.title,
        content=post.content,
        platform=post.platform,
        schedule_time=post.schedule_time,
        is_draft=post.is_draft,
        is_recurring=post.is_recurring,
        recurring_type=post.recurring_type
    )

    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return {
        "message": "Post scheduled successfully",
        "data": new_post
    }


# READ ALL POSTS
@router.get("/schedule")
def get_schedules(db: Session = Depends(get_db)):
    posts = db.query(Post).all()

    return {
        "message": "All posts fetched successfully",
        "data": posts
    }


# GET DRAFT POSTS
@router.get("/drafts")
def get_draft_posts(db: Session = Depends(get_db)):
    drafts = db.query(Post).filter(Post.is_draft == True).all()

    return {
        "message": "Draft posts fetched successfully",
        "data": drafts
    }


# GET RECURRING POSTS
@router.get("/recurring")
def get_recurring_posts(db: Session = Depends(get_db)):
    recurring_posts = db.query(Post).filter(Post.is_recurring == True).all()

    return {
        "message": "Recurring posts fetched successfully",
        "data": recurring_posts
    }


# GET SINGLE POST
@router.get("/schedule/{id}")
def get_schedule(id: int, db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == id).first()

    if not post:
        return {"error": "Post not found"}

    return {
        "data": post
    }


# UPDATE
@router.put("/schedule/{id}")
def update_schedule(id: int, updated_post: PostCreate, db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == id).first()

    if not post:
        return {"error": "Post not found"}

    post.title = updated_post.title
    post.content = updated_post.content
    post.platform = updated_post.platform
    post.schedule_time = updated_post.schedule_time
    post.is_draft = updated_post.is_draft
    post.is_recurring = updated_post.is_recurring
    post.recurring_type = updated_post.recurring_type

    db.commit()
    db.refresh(post)

    return {
        "message": "Post updated successfully",
        "data": post
    }


# DELETE
@router.delete("/schedule/{id}")
def delete_schedule(id: int, db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == id).first()

    if not post:
        return {"error": "Post not found"}

    db.delete(post)
    db.commit()

    return {
        "message": "Post deleted successfully"
    }