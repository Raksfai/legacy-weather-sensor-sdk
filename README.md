# Legacy Weather Sensor SDK

A small Python project for processing weather sensor data in several input
formats. The application identifies the input format, normalizes it into a
single model, calculates weather indicators, and prints a readable report.

## Features

- Supports three sensor data formats.
- Normalizes input into a `WeatherIndicators` object.
- Converts temperatures from Celsius to Fahrenheit.
- Calculates the feels-like temperature.
- Generates a formatted weather report.
- Includes randomized mock data for local demonstrations.

## Requirements

- Python `3.15` or newer.
- [uv](https://docs.astral.sh/uv/).

## Running the Application

Install `uv` if it is not already available, then run:

```bash
uv run main.py
```

The application randomly selects one of the mock datasets and prints the
detected format, normalized data, calculations, and weather report.

## Supported Input Formats

### Sensor 1: String

```text
Kyiv;+10.5C;78%;5.2m/s
```

The values are ordered as city, temperature, humidity, wind speed, and an
optional wind direction.

### Sensor 2: Dictionary

```python
{
    "location": "Kharkiv",
    "data": {
        "temperature": "5.1 C",
        "humidity": "85%",
        "wind": {"speed": "4.5 m/s", "direction": "NW"},
    },
}
```

### Sensor 3: List of Pairs

```python
[
    ("city", "Zaporizhzhia"),
    ("temp_celsius", 9.3),
    ("humidity_percent", 79),
    ("wind_mps", 5.0),
]
```

## Project Structure

| File | Description |
| --- | --- |
| `main.py` | Demonstrates the complete workflow |
| `sensor.py` | Provides mock data and simulates a sensor |
| `data_normalization.py` | Detects formats and normalizes input data |
| `weather_indicators.py` | Defines the weather data model |
| `compute_data.py` | Converts and calculates weather indicators |
| `fancy_output.py` | Builds the formatted text report |

## Example Output

```text
Weather Report for Kharkiv:
Temperature: 5.10°C (41.18°F)
Humidity: 85.00%
Wind Speed: 4.50 m/s
Wind Direction: NW
Feels Like Temperature: 0.41°C
```

## Code Quality Checks

Compile all Python files to check for syntax errors:

```bash
python -m compileall -q .
```

Run the configured `ruff` style checker:

```bash
uv run ruff check .
```
