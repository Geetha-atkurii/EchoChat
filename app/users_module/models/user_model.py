from sqlalchemy import Boolean, Column, Integer, String, DateTime
from datetime import datetime
from sqlalchemy.dialects.mysql import TINYINT
from app.database.base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    username = Column(String(100), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
    full_name = Column(String(150), nullable=True)
    profile_pic = Column(String(255), nullable=True)
    bio = Column(String(500), nullable=True)
    phone = Column(String(20), nullable=True)
    last_seen = Column(DateTime, nullable=True)
    last_login_at = Column(DateTime, nullable=True)
    is_online = Column(Boolean, default=False, nullable=False)
    password_updated_at = Column(DateTime, nullable=True)
    profile_updated_at = Column(DateTime, nullable=True)
    refresh_token = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    is_email_verified = Column(Boolean, default=False, nullable=False)
    created_by = Column(String(255), nullable=True)
    updated_by = Column(String(255), nullable=True)
    is_active = Column(Boolean, default=False, nullable=False)
    is_deleted = Column(Boolean, default=False, nullable=False)