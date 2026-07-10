from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.user import User
from app.schemas.user import UserCreate


async def get_user_by_email(db: AsyncSession, email: str) -> User | None:
    statement = select(User).where(User.email == email)
    result = await db.execute(statement)
    return result.scalars().first()


async def get_user_by_google_sub(db: AsyncSession, google_sub: str) -> User | None:
    statement = select(User).where(User.google_sub == google_sub)
    result = await db.execute(statement)
    return result.scalars().first()


async def create_user(db: AsyncSession, user_create: UserCreate) -> User:
    user = User(
        email=user_create.email,
        full_name=user_create.full_name,
        picture=str(user_create.picture) if user_create.picture else None,
        google_sub=user_create.google_sub,
        is_active=True,
    )
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user


async def sync_user(db: AsyncSession, user_create: UserCreate) -> User:
    user = await get_user_by_google_sub(db, user_create.google_sub)
    if user is None:
        user = await get_user_by_email(db, user_create.email)
    if user is None:
        return await create_user(db, user_create)

    user.email = user_create.email
    user.full_name = user_create.full_name
    user.picture = str(user_create.picture) if user_create.picture else None
    user.google_sub = user_create.google_sub
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user
