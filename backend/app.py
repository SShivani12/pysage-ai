from fastapi import FastAPI

app = FastAPI(
    title="PySage AI",
    description="AI-powered troubleshooting assistant for Python and ML systems.",
    version="0.1.0"
)


@app.get("/")
def root():
    return {
        "message": "Welcome to PySage AI"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "PySage AI",
        "version": "0.1.0"
    }