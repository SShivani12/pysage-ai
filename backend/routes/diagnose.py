from fastapi import APIRouter, UploadFile, File
from backend.services.traceback_parser import parse_traceback
from backend.services.diagnosis_engine import generate_diagnosis

router = APIRouter()


@router.post("/diagnose")
async def diagnose_log(file: UploadFile = File(...)):
    content = await file.read()

    parsed_traceback = parse_traceback(
        content.decode("utf-8")
    )

    diagnosis = generate_diagnosis(parsed_traceback)

    return {
        "traceback": parsed_traceback,
        "diagnosis": diagnosis
    }