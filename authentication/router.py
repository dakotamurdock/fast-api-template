from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

import accounts.schema
from database import db
from authentication import hashing
from accounts.models import Account
from authentication.jwt import create_access_token, get_current_account

router = APIRouter(tags=["auth"])


@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), database: Session = Depends(db.get_db)):
    account = database.query(Account).filter(Account.email == request.username).first()
    if not account:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials")

    if not hashing.verify_password(request.password, account.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid Password")

    access_token = create_access_token(data={"sub": account.email})
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/me", response_model=accounts.schema.DisplayAccount)
def get_current_account(current_account: Account = Depends(get_current_account)):
    account = current_account
    return account
