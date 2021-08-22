import inspect
import re
from typing import Any, Dict, List, Union

from tfl.entities.additional_property import AdditionalProperty
from tfl.entities.place import Place

TYPES = {
    "Tfl.Api.Presentation.Entities.Place": Place,
    "Tfl.Api.Presentation.Entities.AdditionalProperties": AdditionalProperty,
}


def get_type(json: Dict[str, Any]) -> Any:
    if _type := json.get("$type"):
        first, _, _ = _type.partition(",")
        return TYPES[first]
    return None


BASE_TYPES = {"str", "float"}

LST_RE = re.compile(r"List\[(\w+)\]")


def from_json(json: Union[List, Dict]):
    if isinstance(json, list):
        return [from_json_obj(obj) for obj in json]
    return from_json_obj(json)


def from_json_obj(json: Dict[str, Any]):
    entity_type = get_type(json)
    argspec = inspect.getfullargspec(entity_type)

    # Fill out arguments
    class_kwargs = dict()
    for arg in argspec.args[1:]:
        annotation = str(argspec.annotations[arg])
        if annotation in BASE_TYPES:
            class_kwargs[arg] = json[arg]
        else:
            if match := LST_RE.match(annotation):  # it is a list of things
                base_type = match.groups()[0]
                if base_type in BASE_TYPES:
                    class_kwargs[arg] = json.get(arg, None)
                else:
                    collection = []
                    for inner_json in json.get(arg, list()):
                        collection.append(from_json_obj(inner_json))
                    class_kwargs[arg] = collection

    resource = entity_type(**class_kwargs)
    return resource
