from typing import List, Tuple

import requests

from tfl import BASE_URL
from tfl.api.factory import from_json
from tfl.api.presentation.entities.line import Line

ENDPOINT = f"{BASE_URL}/Line"


def by_id(*ids: Tuple[str, ...], status=False, detail=False) -> List[Line]:
    line_ids = ",".join(ids)
    endpoint = f"{ENDPOINT}/{line_ids}" + ("/Status" if status else "")
    endpoint += "?detail=true" if status and detail else ""
    json = requests.get(endpoint).json()
    return from_json(json)


def by_mode(mode: str, status=False) -> List[Line]:
    endpoint = f"{ENDPOINT}/Mode/{mode}" + ("/Status" if status else "")
    json = requests.get(endpoint).json()
    return from_json(json)
