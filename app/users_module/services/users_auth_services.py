from datetime import datetime
from fastapi import HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from app.auth.jwt_handler import JWTHandler
from app.users_module.daos.users_auth_dao import UserDAO
from app.users_module.schemas.user_schema import UserResponse
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
        
        if UserDAO.get_user_by_phone(db, user.phone):
            raise HTTPException(
                status_code=StatusCodes.BAD_REQUEST,
                detail=Messages.PHONE_ALREADY_EXISTS
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
            "phone": user.phone,
            "hashed_password": hashed_password,
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow(),
            "created_by": user_id,
            "updated_by": user_id,
            "is_active": True,
            "is_online": False,
            "is_deleted": False
        }

        user_obj = UserDAO.create_user(db, user_data)

        return user_obj
    
    @staticmethod
    def login_user(db: Session, login_data):

        login = login_data.login_id
        password = login_data.password

        user = UserDAO.get_user_by_login_id(db, login)

        if not user:
            raise HTTPException(status_code=StatusCodes.BAD_REQUEST, detail="Invalid credentials.")

        if not UserAuthUtils.verify_password(password, user.hashed_password):
            raise HTTPException(status_code=StatusCodes.BAD_REQUEST, detail="Invalid credentials")

        user.is_online = True
        user.last_login_at = datetime.utcnow()

        db.add(user)

        token_data = {
            "sub": user.email,
            "user_id": user.user_id
        }

        access_token = JWTHandler.create_access_token(token_data)

        return {
            "user": user,
            "access_token": access_token
        }
    
    @staticmethod
    def fetch_user_profile(user):
        profile_response = UserResponse.model_validate(user)
        return jsonable_encoder(profile_response)