import json
from typing import Any, Iterable


def read_json_file(path: str):
    with open(path) as file:
        data = json.load(file)

    return data
