from fastapi import APIRouter, UploadFile, File
from backend.services.traceback_parser import parse_traceback

router = APIRouter()


@router.post("/diagnose")
async def diagnose(file: UploadFile = File(...)):
    content = await file.read()

    parsed = parse_traceback(content.decode("utf-8"))

    return parsed