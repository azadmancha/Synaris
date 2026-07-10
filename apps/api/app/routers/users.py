from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_current_user
from app.crud.user import sync_user
from app.db import get_db
from app.schemas.user import UserCreate, UserRead

router = APIRouter()


@router.get("/me", response_model=UserRead, summary="Get current user", tags=["users"])
async def read_current_user(current_user=Depends(get_current_user)):
    return current_user


@router.post("/sync", response_model=UserRead, status_code=status.HTTP_201_CREATED, summary="Synchronize the authenticated user profile", tags=["users"])
async def sync_authenticated_user(
    current_user=Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
) -> UserRead:
    user_data = UserCreate(
        email=current_user.email,
        full_name=current_user.full_name,
        picture=current_user.picture,
        google_sub=current_user.google_sub or current_user.email,
    )
    synced = await sync_user(db, user_data)
    return synced
