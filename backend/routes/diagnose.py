from fastapi import APIRouter, UploadFile, File
from backend.services.parser import parse_traceback
from backend.models.schemas import DiagnosisResponse

router = APIRouter()


@router.post("/diagnose", response_model=DiagnosisResponse)
async def diagnose_log(file: UploadFile = File(...)):
    content = await file.read()
    decoded = content.decode("utf-8")

    parsed = parse_traceback(decoded)

    return DiagnosisResponse(
        error_type=parsed["error_type"],
        probable_root_cause=parsed["message"],
        suggested_fixes=[
            "Initial placeholder fix suggestion"
        ],
        confidence=0.55
    )