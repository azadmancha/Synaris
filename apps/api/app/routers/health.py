from fastapi import APIRouter

router = APIRouter()


@router.get("/", summary="Health check", tags=["health"])
async def health():
    return {"status": "ok"}
