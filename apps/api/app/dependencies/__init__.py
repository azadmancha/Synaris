from fastapi import Depends, HTTPException, Request, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import settings
from app.crud.user import get_user_by_email
from app.database import get_db
from app.models.user import User
from app.security.jwt import decode_access_token


auth_scheme = HTTPBearer(auto_error=False)


def _get_authorization_token(request: Request, credentials: HTTPAuthorizationCredentials | None = Depends(auth_scheme)) -> str | None:
    if credentials and credentials.credentials:
        return credentials.credentials
    return request.cookies.get(settings.cookie_name)


async def get_current_user(
    token: str | None = Depends(_get_authorization_token),
    db: AsyncSession = Depends(get_db),
) -> User:
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Missing authentication token")

    try:
        payload = decode_access_token(token)
    except ValueError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authentication token")

    email = payload.get("sub")
    if not email:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authentication payload")

    user = await get_user_by_email(db, email)
    if user is None or not user.is_active:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unable to locate active user")

    return user
