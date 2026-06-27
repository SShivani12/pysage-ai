from backend.services.rules import RULES


def generate_diagnosis(parsed_traceback: dict):
    """
    Generate a diagnosis from parsed traceback information.
    """

    exception = parsed_traceback.get("exception")
    message = parsed_traceback.get("message")

    rule = RULES.get(exception)

    if not rule:
        return {
            "category": "Unknown",
            "root_cause": "Unable to determine the root cause.",
            "confidence": 0.25,
            "suggested_fixes": [
                "Inspect the complete traceback."
            ]
        }

    diagnosis = {
        "rule_id": rule["id"],
        "category": rule["category"],
        "root_cause": rule["root_cause"],
        "confidence": rule["confidence"],
        "suggested_fixes": rule["fixes"]
    }

    # Dynamic handling for ModuleNotFoundError
    if exception == "ModuleNotFoundError" and message:
        package = ""

        if "'" in message:
            package = message.split("'")[1]

        diagnosis["root_cause"] = (
            f"Python package '{package}' is not installed."
        )

        diagnosis["suggested_fixes"] = [
            f"pip install {package}",
            "Verify your virtual environment is activated.",
            f"Run pip show {package}"
        ]

    return diagnosis