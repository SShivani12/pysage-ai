import re


def parse_traceback(log_text: str):
    error_patterns = [
        r"ModuleNotFoundError: (.+)",
        r"ImportError: (.+)",
        r"ValueError: (.+)",
        r"TypeError: (.+)",
        r"RuntimeError: (.+)",
        r"FileNotFoundError: (.+)"
    ]

    for pattern in error_patterns:
        match = re.search(pattern, log_text)
        if match:
            error_type = pattern.split(":")[0]
            return {
                "error_type": error_type,
                "message": match.group(1)
            }

    return {
        "error_type": "Unknown",
        "message": "No recognizable traceback pattern found."
    }