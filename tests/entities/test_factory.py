import pytest

from tfl.api.factory import from_json, from_json_obj


@pytest.fixture
def json():
    return {
        "$type": "Tfl.Api.Presentation.Entities.Place, Tfl.Api.Presentation.Entities",
        "id": "BikePoints_1",
        "url": "/Place/BikePoints_1",
        "commonName": "River Street , Clerkenwell",
        "additionalProperties": [
            {
                "$type": "Tfl.Api.Presentation.Entities.AdditionalProperties, Tfl.Api.Presentation.Entities",
                "category": "Description",
                "key": "TerminalName",
                "sourceSystemKey": "BikePoints",
                "value": "001023",
                "modified": "2021-08-22T07:53:01.157Z",
            },
            {
                "$type": "Tfl.Api.Presentation.Entities.AdditionalProperties, Tfl.Api.Presentation.Entities",
                "category": "Description",
                "key": "Installed",
                "sourceSystemKey": "BikePoints",
                "value": "true",
                "modified": "2021-08-22T07:53:01.157Z",
            },
        ],
        "children": [],
        "childrenUrls": [],
        "placeType": "BikePoint",
        "lat": 51.499606,
        "lon": -0.197574,
    }


def test_from_json_obj(json):
    actual = from_json_obj(json)

    assert actual.lat == 51.499606
    assert actual.additionalProperties[0].value == "001023"


def test_from_json_obj_generic(json):
    actual = from_json(json)

    assert actual.lat == 51.499606
    assert actual.additionalProperties[0].value == "001023"


def test_from_json_generic_as_list(json):
    [actual] = from_json([json])

    assert actual.lat == 51.499606
    assert actual.additionalProperties[0].value == "001023"
