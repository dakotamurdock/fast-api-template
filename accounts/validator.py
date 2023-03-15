from sqlalchemy.orm import Session
from typing import Optional
from fastapi import HTTPException

from . models import Account


async def verify_email_exists(email: str, db_session: Session):
    user = db_session.query(Account).filter(Account.email == email).first()
    if user:
        raise HTTPException(
            status_code=400,
            detail="An account already exists with this email address"
        )


async def verify_active_account(request_account_id: int, active_account_id: int):
    if not request_account_id == active_account_id:
        raise HTTPException(
            status_code=400,
            detail="Changes can only be made to the authenticated account"
        )
