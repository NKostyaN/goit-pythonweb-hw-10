from datetime import date
from typing import Optional
from pydantic import BaseModel, Field, EmailStr, ConfigDict


class ContactSet(BaseModel):
    first_name: str = Field(max_length=50)
    last_name: str = Field(max_length=50)
    email: EmailStr = Field(max_length=100)
    phone: str = Field(max_length=20)
    birthday: date
    info: Optional[str] = Field(max_length=200)


class ContactGet(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: EmailStr
    phone: str
    birthday: date

    model_config = ConfigDict(from_attributes=True)


class ContactUpdate(BaseModel):
    first_name: Optional[str] | None = None
    last_name: Optional[str] | None = None
    email: Optional[EmailStr] | None = None
    phone: Optional[str] | None = None
    birthday: Optional[date] | None = None
    info: Optional[str] | None = None


class User(BaseModel):
    id: int
    username: str
    email: str
    avatar: Optional[str] | None = None

    model_config = ConfigDict(from_attributes=True)


class UserCreate(BaseModel):
    username: str
    email: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class RequestEmail(BaseModel):
    email: EmailStr
