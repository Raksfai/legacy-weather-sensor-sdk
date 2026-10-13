BEAUFORT_SPEED_THRESHOLDS_MPS = (0.3, 1.6, 3.4, 5.5, 8.0, 10.8)
BEAUFORT_DESCRIPTIONS = (
    "Calm",
    "Light air",
    "Light breeze",
    "Gentle breeze",
    "Moderate breeze",
    "Fresh breeze",
)
STRONG_WIND_WARNING = "Strong wind (warning)"


def classify_wind_speed(wind_speed_mps: float) -> str:
    if wind_speed_mps < 0:
        raise ValueError("wind speed cannot be negative")

    for threshold, description in zip(
        BEAUFORT_SPEED_THRESHOLDS_MPS, BEAUFORT_DESCRIPTIONS, strict=True
    ):
        if wind_speed_mps < threshold:
            return description

    return STRONG_WIND_WARNING
