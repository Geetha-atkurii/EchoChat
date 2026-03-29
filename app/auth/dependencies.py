from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session

from app.core.dependencies import get_db
from app.auth.jwt_handler import JWTHandler
from app.users_module.daos.users_auth_dao import UserDAO

security = HTTPBearer()


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
):
    token = credentials.credentials

    try:
        payload = JWTHandler.decode_token(token)
        email = payload.get("sub")

        if not email:
            raise HTTPException(status_code=401, detail="Invalid token")

    except Exception:
        raise HTTPException(status_code=401, detail="Token expired or invalid")

    user = UserDAO.get_user_by_email(db, email)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user