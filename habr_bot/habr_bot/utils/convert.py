from io import BytesIO

import json


def bytes_to_string(data: BytesIO) -> str:
    bytes_data = data.read()
    return bytes_data.decode()


def string_to_json(data: str) -> dict:
    try:
        return json.loads(data)
    except json.JSONDecodeError:
        return {}
