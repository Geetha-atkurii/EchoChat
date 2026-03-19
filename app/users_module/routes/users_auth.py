from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.dependencies import get_db
from app.users_module.schemas.user_schema import UserCreate
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
            message=Messages.INTERNAL_SERVER_ERROR,
            status_code=StatusCodes.INTERNAL_SERVER_ERROR,
            data=None
        )