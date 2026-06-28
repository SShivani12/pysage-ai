def detect_input_type(text: str) -> str:
    """
    Detect the type of uploaded file based on its contents.
    """

    text_lower = text.lower()

    # Python traceback
    if "traceback (most recent call last)" in text_lower:
        return "traceback"

    # requirements.txt
    if "==" in text:
        return "requirements"

    return "unknown"