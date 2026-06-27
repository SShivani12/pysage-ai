import re


def parse_traceback(log_text: str):
    """
    Extract useful information from a Python traceback.
    """

    result = {
        "file": None,
        "line": None,
        "exception": None,
        "message": None
    }

    # ----------------------------
    # File and line number
    # ----------------------------
    file_match = re.search(
        r'File "(.+?)", line (\d+)',
        log_text
    )

    if file_match:
        result["file"] = file_match.group(1)
        result["line"] = int(file_match.group(2))

    # ----------------------------
    # Last line = Exception
    # ----------------------------
    last_line = log_text.strip().split("\n")[-1]

    if ":" in last_line:
        exception, message = last_line.split(":", 1)

        result["exception"] = exception.strip()
        result["message"] = message.strip()

    return result