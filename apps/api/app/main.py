from fastapi import FastAPI

app = FastAPI(title="Synaris API")

@app.get("/health")
def health():
    return {"status": "ok"}
