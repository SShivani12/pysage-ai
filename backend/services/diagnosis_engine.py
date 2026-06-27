def generate_diagnosis(parsed_traceback: dict):
    """
    Generate a diagnosis from parsed traceback information.
    """

    exception = parsed_traceback.get("exception")
    message = parsed_traceback.get("message")

    # -----------------------------
    # Rule 1
    # Missing package
    # -----------------------------
    if exception == "ModuleNotFoundError":

        package = ""

        if "'" in message:
            package = message.split("'")[1]

        return {
            "category": "Missing Dependency",
            "root_cause": f"Python package '{package}' is not installed.",
            "confidence": 0.98,
            "suggested_fixes": [
                f"pip install {package}",
                "Verify your virtual environment is activated.",
                "Run pip show " + package
            ]
        }

    # -----------------------------
    # Default
    # -----------------------------
    return {
        "category": "Unknown",
        "root_cause": "Unable to determine the root cause.",
        "confidence": 0.25,
        "suggested_fixes": [
            "Inspect the complete traceback."
        ]
    }