from backend.services.analysis_pipeline import analyze_input
from backend.services.analysis_pipeline import analyze_input
from backend.services.dependency_analyzer import analyze_dependencies
from fastapi import APIRouter, UploadFile, File

from backend.services.traceback_parser import parse_traceback
from backend.services.diagnosis_engine import generate_diagnosis
from backend.services.requirements_parser import parse_requirements

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


@router.post("/analyze-requirements")
async def analyze_requirements(file: UploadFile = File(...)):
    content = await file.read()

    parsed_requirements = parse_requirements(
        content.decode("utf-8")
    )

    dependency_analysis = analyze_dependencies(
        parsed_requirements
    )

    return {
        "packages": parsed_requirements["packages"],
        "analysis": dependency_analysis
    }
@router.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    content = await file.read()

    result = analyze_input(
        content.decode("utf-8")
    )

    return result
@router.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    """
    Unified analysis endpoint.
    Automatically detects the uploaded file type and routes it
    through the appropriate analysis pipeline.
    """

    content = await file.read()

    result = analyze_input(
        content.decode("utf-8")
    )

    return result
