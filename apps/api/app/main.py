from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.database import Base, engine
from app.middleware.security import SecurityHeadersMiddleware, SimpleRateLimitMiddleware
from app.routers.ai import router as ai_router
from app.routers.health import router as health_router
from app.routers.users import router as users_router


app = FastAPI(title=settings.project_name)
app.add_middleware(SecurityHeadersMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.app_url],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(SimpleRateLimitMiddleware)
app.include_router(health_router, prefix="/health")
app.include_router(users_router, prefix="/users")
app.include_router(ai_router, prefix="/ai")


@app.on_event("startup")
async def on_startup() -> None:
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)
