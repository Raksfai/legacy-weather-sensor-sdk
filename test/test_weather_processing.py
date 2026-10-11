import pytest

from compute_data import (
    convert_celsius_to_fahrenheit,
    convert_temperature_to_feels_like,
)
from data_normalization import (
    normalize_raw_data_from_dict,
    normalize_raw_data_from_list,
    normalize_raw_data_from_string,
)
from fancy_output import make_fancy_output
from weather_indicators import WeatherIndicators


def test_normalize_raw_data_from_string() -> None:
    result = normalize_raw_data_from_string("Kyiv;+10.5C;78%;5.2m/s")

    assert result == WeatherIndicators("Kyiv", 10.5, 78.0, 5.2)


def test_normalize_raw_data_from_dict() -> None:
    raw_data = {
        "location": "Kharkiv",
        "data": {
            "temperature": "5.1 C",
            "humidity": "85%",
            "wind": {"speed": "4.5 m/s", "direction": "NW"},
        },
    }
    result = normalize_raw_data_from_dict(raw_data)

    assert result == WeatherIndicators("Kharkiv", 5.1, 85.0, 4.5, "NW")


def test_normalize_raw_data_from_list() -> None:
    raw_data = [
        ("city", "Zaporizhzhia"),
        ("temp_celsius", 9.3),
        ("humidity_percent", 79),
        ("wind_mps", 5.0),
    ]
    result = normalize_raw_data_from_list(raw_data)

    assert result == WeatherIndicators("Zaporizhzhia", 9.3, 79.0, 5.0)


@pytest.mark.parametrize(
    ("weather_data", "expected"),
    [
        (WeatherIndicators("Kyiv", 0, 0, 0), 32.0),
        (WeatherIndicators("Lviv", 100, 0, 0), 212.0),
        (WeatherIndicators("Odesa", -40, 0, 0), -40.0),
    ],
)
def test_convert_celsius_to_fahrenheit(
    weather_data: WeatherIndicators, expected: float
) -> None:
    assert convert_celsius_to_fahrenheit(weather_data) == expected


@pytest.mark.parametrize(
    ("weather_data", "expected"),
    [
        (WeatherIndicators("Kyiv", 10, 50, 5), 4.52),
        (WeatherIndicators("Lviv", 20, 70, 3), 19.29),
        (WeatherIndicators("Odesa", -5, 80, 10), -14.89),
    ],
)
def test_convert_temperature_to_feels_like(
    weather_data: WeatherIndicators, expected: float
) -> None:
    assert convert_temperature_to_feels_like(weather_data) == expected


def test_make_fancy_output() -> None:
    data = WeatherIndicators("Kyiv", 10, 50, 5, "NE")
    output = make_fancy_output(data)

    expected_output = (
        "Weather Report for Kyiv:\n"
        "Temperature: 10.00°C (50.00°F)\n"
        "Humidity: 50.00%\n"
        "Wind Speed: 5.00 m/s\n"
        "Wind Direction: NE\n"
        "Feels Like Temperature: 4.52°C"
    )

    assert output == expected_output
