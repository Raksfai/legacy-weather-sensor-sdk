from weather_indicators import WeatherIndicators

FAHRENHEIT_OFFSET = 32
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5.0

HUMIDITY_PERCENT_DIVISOR = 100.0
VAPOR_PRESSURE_BASE = 6.105
EXPONENTIAL_BASE = 2.71828
TEMPERATURE_COEFFICIENT = 17.27
TEMPERATURE_OFFSET = 237.7
VAPOR_PRESSURE_COEFFICIENT = 0.33
WIND_COEFFICIENT = 0.7
APPARENT_TEMPERATURE_OFFSET = 4.0


def convert_celsius_to_fahrenheit(weather_data: WeatherIndicators) -> float:
    return round(
        (weather_data.temperature_celsius * CELSIUS_TO_FAHRENHEIT_FACTOR)
        + FAHRENHEIT_OFFSET,
        2,
    )


def convert_temperature_to_feels_like(weather_data: WeatherIndicators) -> float:

    vapor_pressure = calculate_vapor_pressure(weather_data)

    feels_like = (
        weather_data.temperature_celsius
        + VAPOR_PRESSURE_COEFFICIENT * vapor_pressure
        - WIND_COEFFICIENT * weather_data.wind_speed
        - APPARENT_TEMPERATURE_OFFSET
    )

    return round(feels_like, 2)


def calculate_vapor_pressure(weather_data):
    vapor_pressure = (
        (weather_data.humidity_percent / HUMIDITY_PERCENT_DIVISOR)
        * VAPOR_PRESSURE_BASE
        * (
            EXPONENTIAL_BASE
            ** (
                (TEMPERATURE_COEFFICIENT * weather_data.temperature_celsius)
                / (TEMPERATURE_OFFSET + weather_data.temperature_celsius)
            )
        )
    )
    return vapor_pressure
