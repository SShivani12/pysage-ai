from fastapi import FastAPI
from backend.routes.diagnose import router as diagnose_router
from backend.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "PySage AI"
    }


app.include_router(diagnose_router, prefix="/api")