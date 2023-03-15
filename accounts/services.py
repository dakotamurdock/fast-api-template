from typing import Optional
from fastapi import HTTPException, status

from . import models
from authentication import hashing


async def register_new_account(request, database) -> models.Account:
    """Function to create a new account in the accounts database"""
    new_account = models.Account(name=request.name,
                                 email=request.email,
                                 password=request.password
                                 )
    database.add(new_account)
    database.commit()
    database.refresh(new_account)
    return new_account


async def get_account_by_id(account_id, database) -> Optional[models.Account]:
    """Function to retrieve account data from the accounts table excluding password"""
    account_info = database.query(models.Account).get(account_id)
    if not account_info:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Account Not Found")
    return account_info


async def update_account_by_id(account_id, request, database):
    """Function to update specified fields in the accounts table with new values"""
    account_data = await get_account_by_id(account_id, database)
    update_account_data = request.dict(exclude_unset=True)
    for key, value in update_account_data.items():
        if key == 'password':
            value = hashing.get_password_hash(value)
        setattr(account_data, key, value)
    database.add(account_data)
    database.commit()
    database.refresh(account_data)
    return account_data


async def delete_account_by_id(account_id, database):
    """Function to remove an account from the accounts table"""
    database.query(models.Account).filter(models.Account.id == account_id).delete()
    database.commit()
