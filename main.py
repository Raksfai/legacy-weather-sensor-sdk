import sensor
from compute_data import (
    convert_celsius_to_fahrenheit,
    convert_temperature_to_feels_like,
)
from data_normalization import identify_sensor_format, normalize_raw_data
from fancy_output import make_fancy_output

SEPARATOR_LENGTH = 20

raw_data = sensor.get_raw_data()

print("\nFirst task")

print("=" * SEPARATOR_LENGTH)
print(identify_sensor_format(raw_data))
print("=" * SEPARATOR_LENGTH)

data = normalize_raw_data(raw_data)


print("\nSecond task")

print("=" * SEPARATOR_LENGTH)
print(data.__dict__)
print("=" * SEPARATOR_LENGTH)

print("\nThird task")

print("=" * SEPARATOR_LENGTH)
print("Celsius to Fahrenheit: " + str(convert_celsius_to_fahrenheit(data)))
print("Feels like: " + str(convert_temperature_to_feels_like(data)))
print("=" * SEPARATOR_LENGTH)

print("\nFourth task")

print("=" * SEPARATOR_LENGTH)
print(make_fancy_output(data))
print("=" * SEPARATOR_LENGTH)
