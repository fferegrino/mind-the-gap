from tfl.api.bike_point import by_bounds, by_radius, search


def test_by_bounds():
    # There is a single station in the following coordinates
    sw_lat = 51.497330
    sw_lon = -0.050831
    ne_lat = 51.499026
    ne_lon = -0.046816
    [place] = by_bounds(sw_lat, sw_lon, ne_lat, ne_lon)

    assert place.commonName == "Canada Water Station, Rotherhithe"
    assert place.lat == 51.498439
    assert place.lon == -0.04915


def test_by_radius():
    # There is a single station in the following coordinates
    places_response = by_radius(lat=51.487167, lon=-0.008654, radius=200)

    [place] = places_response.places
    assert place.commonName == "Saunders Ness Road, Cubitt Town"
    assert place.lat == 51.487129
    assert place.lon == -0.009001


def test_search():
    [westminster] = search("Westminster Pier, Westminster")
    assert westminster.commonName == "Westminster Pier, Westminster"
