from fastapi import APIRouter, HTTPException

from app.schemas.ai import AIRequest, AIResponse
from services.ai import AIOrchestrator

router = APIRouter(tags=["ai"])
orchestrator = AIOrchestrator()


@router.get("/health", summary="AI provider health check")
async def ai_health() -> dict[str, object]:
    try:
        providers = await orchestrator.health()
    except ValueError as exc:
        raise HTTPException(status_code=503, detail=str(exc))
    return {"status": "ok", "providers": providers}


@router.post("/generate", response_model=AIResponse, summary="Generate text from an AI provider")
async def generate_text(request: AIRequest) -> AIResponse:
    try:
        text = await orchestrator.generate_text(
            request.prompt,
            provider=request.provider,
            max_tokens=request.max_tokens or 512,
            temperature=request.temperature or 0.3,
        )
    except Exception as exc:
        raise HTTPException(status_code=502, detail=str(exc))

    return AIResponse(provider=request.provider or orchestrator.default_provider, text=text)
