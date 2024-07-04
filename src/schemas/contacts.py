
from typing import Optional
from datetime import date
from pydantic import BaseModel, EmailStr, Field, EmailStr


class ContactSchema(BaseModel):
    full_name: str = Field(min_length=3, max_length=50)
    email: EmailStr
    phone_number:  str = Field(min_length=10)
    birthday: date


class ContactUpdateSchema(ContactSchema):
    phone_number: str = Field(min_length=10)
    birthday: date


class ContactResponse(BaseModel):
    id: int = 1
    full_name: str
    email: str
    phone_number:  str
    birthday: date

    class Config:
        from_attributes = True
