from dataclasses import dataclass


@dataclass
class WeatherIndicators:
    city: str
    temperature_celsius: float
    humidity_percent: float
    wind_speed: float
    wind_direction: str | None = None
