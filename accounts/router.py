"""
When you want to create a new API endpoint for accounts, create the function here
"""

from fastapi import APIRouter, Depends, status, Response
from sqlalchemy.orm import Session

from . import schema
from database import db
from . import services
from . import validator
from authentication import jwt

router = APIRouter(tags=['accounts'], prefix='/accounts')


@router.post('/', status_code=status.HTTP_201_CREATED)
async def account_registration(request: schema.Account, database: Session = Depends(db.get_db)):

    # Perform validations before creating account
    await validator.verify_email_exists(request.email, database)

    # If validations are passed, proceed with creating account
    return await services.register_new_account(request, database)


@router.get('/{account_id}', status_code=status.HTTP_200_OK, response_model=schema.DisplayAccount)
async def get_account_by_id(account_id: int, database: Session = Depends(db.get_db)):
    return await services.get_account_by_id(account_id, database)


@router.patch("/{account_id}", status_code=status.HTTP_200_OK, response_model=schema.DisplayAccount)
async def update_account_by_id(account_id: int,
                               request: schema.UpdateAccount,
                               active_account: schema.DisplayAccount = Depends(jwt.get_current_account),
                               database: Session = Depends(db.get_db),
                               token: str = Depends(jwt.oauth2_scheme)
                               ):
    active_account_id = active_account.id
    request_account_id = account_id
    await validator.verify_active_account(request_account_id, active_account_id)
    # await services.update_account_by_id(account_id, request, database)
    return await services.update_account_by_id(account_id, request, database)


@router.delete('/{account_id}', status_code=status.HTTP_204_NO_CONTENT, response_class=Response)
async def delete_account_by_id(account_id: int,
                               active_account: schema.DisplayAccount = Depends(jwt.get_current_account),
                               database: Session = Depends(db.get_db),
                               token: str = Depends(jwt.oauth2_scheme)
                               ):
    active_account_id = active_account.id
    request_account_id = account_id
    await validator.verify_active_account(request_account_id, active_account_id)
    await services.delete_account_by_id(account_id, database)
    # return await services.delete_account_by_id(account_id, database)
