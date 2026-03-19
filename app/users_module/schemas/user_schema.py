from typing import Optional
from datetime import datetime
from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: EmailStr
    username: str
    full_name: Optional[str] = None
    profile_pic: Optional[str] = None
    bio: Optional[str] = None
    phone: Optional[str] = None


class UserCreate(BaseModel):
    email: EmailStr
    username: str
    password: str


class UserUpdate(BaseModel):
    full_name: Optional[str] = None
    profile_pic: Optional[str] = None
    bio: Optional[str] = None
    phone: Optional[str] = None

    class Config:
        from_attributes = True


class UserResponse(BaseModel):
    id: int
    user_id: str
    email: str
    username: str
    full_name: Optional[str]
    profile_pic: Optional[str]
    bio: Optional[str]
    phone: Optional[str]
    last_seen: Optional[datetime]
    last_login_at: Optional[datetime]
    is_online: Optional[int]
    password_updated_at: Optional[datetime]
    profile_updated_at: Optional[datetime]
    created_at: datetime
    updated_at: datetime
    created_by: Optional[int]
    updated_by: Optional[int]
    is_active: Optional[int]
    is_email_verified: Optional[int]
    is_deleted: Optional[int]

    class Config:
        from_attributes = True


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserLoginResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


class ForgotPasswordRequest(BaseModel):
    email: EmailStr


class ResetPasswordRequest(BaseModel):
    token: str
    new_password: str


class ChangePasswordRequest(BaseModel):
    old_password: str
    new_password: str


class UserFilterRequest(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None
    is_online: Optional[bool] = None