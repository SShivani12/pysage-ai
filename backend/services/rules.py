RULES = {
    "ModuleNotFoundError": {
        "category": "Missing Dependency",
        "confidence": 0.98,
        "root_cause": "Required Python package is not installed.",
        "fixes": [
            "Install the missing package using pip.",
            "Verify the virtual environment is activated.",
            "Confirm the package is installed with 'pip show'."
        ]
    },

    "ImportError": {
        "category": "Import Error",
        "confidence": 0.92,
        "root_cause": "Python could not import the requested module or object.",
        "fixes": [
            "Check the installed package version.",
            "Verify import syntax.",
            "Read the library release notes."
        ]
    },

    "FileNotFoundError": {
        "category": "File System",
        "confidence": 0.95,
        "root_cause": "Specified file or directory does not exist.",
        "fixes": [
            "Verify the file path.",
            "Check the working directory.",
            "Confirm the file exists."
        ]
    },

    "TypeError": {
        "category": "Programming Error",
        "confidence": 0.90,
        "root_cause": "An operation received an unexpected object type.",
        "fixes": [
            "Inspect variable types.",
            "Review function arguments.",
            "Use isinstance() for debugging."
        ]
    }
}