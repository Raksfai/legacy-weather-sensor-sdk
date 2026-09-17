from compute_data import (
    convert_celsius_to_fahrenheit,
    convert_temperature_to_feels_like,
)
from weather_indicators import WeatherIndicators


def make_fancy_output(data: WeatherIndicators) -> str:
    output = f"Weather Report for {data.city}:\n"
    output += f"Temperature: {data.temperature_celsius:.2f}°C ({convert_celsius_to_fahrenheit(data):.2f}°F)\n"
    output += f"Humidity: {data.humidity_percent:.2f}%\n"
    output += f"Wind Speed: {data.wind_speed:.2f} m/s\n"
    if data.wind_direction is not None:
        output += f"Wind Direction: {data.wind_direction}\n"
    output += f"Feels Like Temperature: {convert_temperature_to_feels_like(data):.2f}°C"
    return output
