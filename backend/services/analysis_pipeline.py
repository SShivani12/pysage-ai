from backend.services.input_detector import detect_input_type
from backend.services.traceback_parser import parse_traceback
from backend.services.diagnosis_engine import generate_diagnosis

from backend.services.requirements_parser import parse_requirements
from backend.services.dependency_analyzer import analyze_dependencies


def analyze_input(text: str):
    """
    Main analysis pipeline.
    Detects input type and routes it to the correct parser/analyzer.
    """

    input_type = detect_input_type(text)

    # -----------------------------
    # Traceback pipeline
    # -----------------------------
    if input_type == "traceback":

        parsed = parse_traceback(text)

        diagnosis = generate_diagnosis(parsed)

        return {
            "input_type": input_type,
            "parsed_data": parsed,
            "analysis": diagnosis
        }

    # -----------------------------
    # Requirements pipeline
    # -----------------------------
    elif input_type == "requirements":

        parsed = parse_requirements(text)

        analysis = analyze_dependencies(parsed)

        return {
            "input_type": input_type,
            "parsed_data": parsed,
            "analysis": analysis
        }

    # -----------------------------
    # Unknown
    # -----------------------------
    return {
        "input_type": "unknown",
        "parsed_data": None,
        "analysis": {
            "message": "Unsupported input type."
        }
    }