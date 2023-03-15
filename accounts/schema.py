"""
API Response model with Pydantic
Specify the models returned by the API to the client
"""

from pydantic import BaseModel, constr, EmailStr
from typing import Optional


class Account(BaseModel):
    name: constr(min_length=1, max_length=250)
    email: EmailStr
    password: constr(min_length=8, max_length=50)


class DisplayAccount(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        orm_mode = True


class UpdateAccount(BaseModel):
    name: Optional[constr(min_length=1, max_length=250)] = None
    email: Optional[EmailStr] = None
    password: Optional[constr(min_length=8, max_length=50)] = None
