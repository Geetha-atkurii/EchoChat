from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.auth.dependencies import get_current_user
from app.core.config import Settings
from app.core.dependencies import get_db
from app.users_module.models.user_model import User
from app.users_module.schemas.user_schema import UserCreate, UserLogin
from app.users_module.services.users_auth_services import UserAuthService
from app.utils.constants import Messages, StatusCodes
from app.custom_response.custom_response import success_response, error_response

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register")
async def register(user: UserCreate, db: Session = Depends(get_db)):
    try:
        user_obj = UserAuthService.register_user(db, user)
        db.commit()
        db.refresh(user_obj)

        return success_response(
            message=Messages.USER_CREATED,
            status_code=StatusCodes.CREATED,
            data={"user_name": user_obj.username, "email": user_obj.email}
        )

    except HTTPException as e:
        db.rollback()
        return error_response(
            message=e.detail,
            status_code=e.status_code,
            data=None
        )

    except Exception as e:
        db.rollback()
        return error_response(
            message=str(e) if Settings.DEBUG else Messages.INTERNAL_SERVER_ERROR,
            status_code=StatusCodes.INTERNAL_SERVER_ERROR,
            data=None
        )

@router.post("/login")
async def login(login_data: UserLogin, db: Session = Depends(get_db)):

    try:
        result = UserAuthService.login_user(db, login_data)

        db.commit()

        return success_response(
            message=Messages.LOGIN_SUCCESS,
            status_code=StatusCodes.SUCCESS,
            data={
                "access_token": result["access_token"],
                "token_type": "bearer"
            }
        )

    except HTTPException as e:
        db.rollback()
        return error_response(
            message=e.detail,
            status_code=e.status_code,
            data=None
        )

    except Exception as e:
        db.rollback()
        print("LOGIN_ERROR===>", e)
        return error_response(
            message=str(e) if Settings.DEBUG else Messages.INTERNAL_SERVER_ERROR,
            status_code=StatusCodes.INTERNAL_SERVER_ERROR,
            data=None
        )
    
@router.get("/user_profile")
async def get_user_profile(current_user: User = Depends(get_current_user)):
    try:
        result = UserAuthService.fetch_user_profile(current_user)

        return success_response(
            message=Messages.USER_PROFILE_FETCHED,
            status_code=StatusCodes.SUCCESS,
            data=result
        )

    except HTTPException as e:
        return error_response(
            message=e.detail,
            status_code=e.status_code,
            data=None
        )

    except Exception as e:
        print("PROFILE_FETCH_ERROR===>", e)
        return error_response(
            message=str(e) if Settings.DEBUG else Messages.INTERNAL_SERVER_ERROR,
            status_code=StatusCodes.INTERNAL_SERVER_ERROR,
            data=None
        )