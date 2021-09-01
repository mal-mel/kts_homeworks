def validate_json(data: dict) -> bool:
    if "links" in data and "tags" in data:
        if isinstance(data["links"], list) and isinstance(data["tags"], list):
            return True
    return False
