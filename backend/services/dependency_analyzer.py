def analyze_dependencies(parsed_requirements: dict):
    """
    Analyze parsed requirements for common dependency issues.
    """

    packages = parsed_requirements.get("packages", [])

    total_packages = len(packages)

    unpinned_packages = []
    duplicate_packages = []

    seen = set()

    for package in packages:

        name = package["name"]
        version = package["version"]

        # Detect duplicate packages
        if name in seen:
            duplicate_packages.append(name)
        else:
            seen.add(name)

        # Detect packages without versions
        if version is None:
            unpinned_packages.append(name)

    return {
        "summary": {
            "total_packages": total_packages,
            "duplicate_packages": len(duplicate_packages),
            "unpinned_packages": len(unpinned_packages)
        },
        "duplicates": duplicate_packages,
        "unpinned": unpinned_packages
    }