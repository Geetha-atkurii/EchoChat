from datetime import datetime
from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.users_module.daos.users_auth_dao import UserDAO
from app.utils.constants import Messages, StatusCodes
from app.utils.utils import UserAuthUtils

class UserAuthService:

    @staticmethod
    def register_user(db: Session, user):

        email = user.email.lower()

        if user.password != user.confirm_password:
            raise HTTPException(status_code=StatusCodes.BAD_REQUEST, detail=Messages.CONFIRM_PASSWORD_VALIDATION_ERROR)

        if UserDAO.get_user_by_email(db, email):
            raise HTTPException(
                status_code=StatusCodes.BAD_REQUEST,
                detail=Messages.USER_ALREADY_EXISTS
            )

        if UserDAO.get_user_by_username(db, user.username):
            raise HTTPException(
                status_code=StatusCodes.BAD_REQUEST,
                detail=Messages.USERNAME_ALREADY_EXISTS
            )

        try:
            UserAuthUtils.validate_password(user.password)
        except ValueError as e:
            raise HTTPException(status_code=StatusCodes.BAD_REQUEST, detail=str(e))

        hashed_password = UserAuthUtils.hash_password(user.password)
        user_id = UserAuthUtils.generate_user_id()

        user_data = {
            "user_id": user_id,
            "email": email,
            "username": user.username,
            "hashed_password": hashed_password,
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow(),
            "created_by": user_id,
            "updated_by": user_id,
            "is_active": False,
            "is_deleted": False,
            "is_email_verified": False
        }

        user_obj = UserDAO.create_user(db, user_data)

        return user_obj