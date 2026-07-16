from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.social_account import SocialAccount
from app.models.user import User
from app.schemas.social_account import (
    SocialAccountCreate,
    SocialAccountResponse,
)
from app.core.dependencies import get_current_user

router = APIRouter(
    prefix="/social-accounts",
    tags=["Social Accounts"],
)


@router.post("/", response_model=SocialAccountResponse)
def create_social_account(
    account: SocialAccountCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    new_account = SocialAccount(
        user_id=current_user.id,
        platform_name=account.platform_name,
        profile_name=account.profile_name,
    )

    db.add(new_account)
    db.commit()
    db.refresh(new_account)

    return new_account


@router.get("/", response_model=list[SocialAccountResponse])
def get_social_accounts(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return (
        db.query(SocialAccount)
        .filter(SocialAccount.user_id == current_user.id)
        .all()
    )


@router.delete("/{account_id}")
def delete_social_account(
    account_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    account = (
        db.query(SocialAccount)
        .filter(
            SocialAccount.id == account_id,
            SocialAccount.user_id == current_user.id,
        )
        .first()
    )

    if not account:
        raise HTTPException(
            status_code=404,
            detail="Social account not found",
        )

    db.delete(account)
    db.commit()

    return {"message": "Social account deleted successfully"}