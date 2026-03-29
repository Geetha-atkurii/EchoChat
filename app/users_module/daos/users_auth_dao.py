import logging
from sqlalchemy import or_
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from app.users_module.models.user_model import User

logger = logging.getLogger(__name__)

class UserDAO:

    @staticmethod
    def get_user_by_email(db: Session, email: str):
        return db.query(User).filter(
            User.email == email,
            User.is_deleted == False
        ).first()

    @staticmethod
    def get_user_by_username(db: Session, username: str):
        return db.query(User).filter(
            User.username == username,
            User.is_deleted == False
        ).first()

    @staticmethod
    def get_user_by_phone(db: Session, phone: str):
        return db.query(User).filter(
            User.phone == phone,
            User.is_deleted == False
        ).first()

    @staticmethod
    def create_user(db: Session, user_data: dict):
        user = User(**user_data)
        db.add(user)
        return user

    @staticmethod
    def get_user_by_login_id(db: Session, login_id: str):
        return db.query(User).filter(
            or_(
                User.email == login_id,
                User.username == login_id,
                User.phone == login_id
            ),
            User.is_deleted == False
        ).first()
    
    @staticmethod
    def get_user_by_user_id(db: Session, user_id: str):
        return db.query(User).filter(
            User.user_id == user_id,
            User.is_deleted == False
        ).first()