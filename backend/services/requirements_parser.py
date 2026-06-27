def parse_requirements(requirements_text: str):
    """
    Parse a requirements.txt file into structured package information.
    """

    packages = []

    lines = requirements_text.splitlines()

    for line in lines:
        line = line.strip()

        # Ignore empty lines and comments
        if not line or line.startswith("#"):
            continue

        if "==" in line:
            name, version = line.split("==", 1)

            packages.append({
                "name": name.strip(),
                "version": version.strip()
            })

        else:
            packages.append({
                "name": line,
                "version": None
            })

    return {
        "packages": packages
    }