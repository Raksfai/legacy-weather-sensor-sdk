from weather_indicators import WeatherIndicators

CITY_INDEX = 0
TEMP_CELSIUS_INDEX = 1
HUMIDITY_PERCENT_INDEX = 2
WIND_SPEED_INDEX = 3
WIND_DIRECTION_INDEX = 4


def identify_sensor_format(raw_data: str | dict | list) -> str:
    if isinstance(raw_data, str):
        return "string type (Sensor 1)"
    if isinstance(raw_data, dict):
        return "dict type (Sensor 2)"
    if isinstance(raw_data, list):
        return "list type (Sensor 3)"
    return "Unknown format"


def normalize_raw_data_from_string(raw_data: str) -> WeatherIndicators:
    derived_data = raw_data.split(";")
    return WeatherIndicators(
        derived_data[CITY_INDEX],
        float(derived_data[TEMP_CELSIUS_INDEX].rstrip("C").strip()),
        float(derived_data[HUMIDITY_PERCENT_INDEX].rstrip("%")),
        float(derived_data[WIND_SPEED_INDEX].rstrip("m/s").strip()),
        derived_data[WIND_DIRECTION_INDEX]
        if len(derived_data) > WIND_DIRECTION_INDEX
        else None,
    )


def normalize_raw_data_from_dict(raw_data: dict) -> WeatherIndicators:
    return WeatherIndicators(
        raw_data["location"],
        float(raw_data["data"]["temperature"].rstrip(" C")),
        float(raw_data["data"]["humidity"].rstrip("%")),
        float(raw_data["data"]["wind"]["speed"].rstrip(" m/s").strip()),
        raw_data["data"]["wind"]["direction"],
    )


def normalize_raw_data_from_list(raw_data: list) -> WeatherIndicators:
    return WeatherIndicators(
        raw_data[CITY_INDEX][1],
        float(raw_data[TEMP_CELSIUS_INDEX][1]),
        float(raw_data[HUMIDITY_PERCENT_INDEX][1]),
        float(raw_data[WIND_SPEED_INDEX][1]),
        raw_data[WIND_DIRECTION_INDEX][1]
        if len(raw_data) > WIND_DIRECTION_INDEX
        else None,
    )


def normalize_raw_data(raw_data: str | dict | list) -> WeatherIndicators:
    if isinstance(raw_data, str):
        return normalize_raw_data_from_string(raw_data)
    if isinstance(raw_data, dict):
        return normalize_raw_data_from_dict(raw_data)
    if isinstance(raw_data, list):
        return normalize_raw_data_from_list(raw_data)
    raise ValueError(f"Unknown sensor data format: {type(raw_data).__name__}")
