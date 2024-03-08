import pytest
import requests_mock
from requests.exceptions import HTTPError
from weather_sdk import WeatherSDK, API_KEY


@pytest.fixture
def weather_sdk():
    return WeatherSDK(API_KEY)


def test_get_weather_by_city_http_error(weather_sdk):
    city_name = "NonexistentCity"
    with requests_mock.Mocker() as m:
        m.get(requests_mock.ANY, status_code=404)
        with pytest.raises(HTTPError):
            weather_sdk.get_weather_by_city(city_name)
