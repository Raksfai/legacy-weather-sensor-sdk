from dataclasses import dataclass


@dataclass
class WeatherIndicators:
    def __init__(
        self,
        city: str,
        temperature_celsius: float,
        humidity_percent: float,
        wind_speed: float,
        wind_direction: str | None = None,
    ):
        self.city = city
        self.temperature_celsius = temperature_celsius
        self.humidity_percent = humidity_percent
        self.wind_speed = wind_speed
        self.wind_direction: str | None = wind_direction
