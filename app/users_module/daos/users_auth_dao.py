import logging
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
    def create_user(db: Session, user_data: dict):
        user = User(**user_data)
        db.add(user)
        return user