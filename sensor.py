import random

_MOCK_DATA = [
    # Sensor 1 data format
    "Kyiv;+10.5C;78%;5.2m/s",
    "Lviv;-1.2C;92%;2.1m/s",
    "Odesa;+15.0C;65%;7.8m/s",
    # Sensor 2 data format
    {
        "location": "Kharkiv",
        "data": {
            "temperature": "5.1 C",
            "humidity": "85%",
            "wind": {"speed": "4.5 m/s", "direction": "NW"},
        },
    },
    {
        "location": "Dnipro",
        "data": {
            "temperature": "7.8 C",
            "humidity": "77%",
            "wind": {"speed": "3.9 m/s", "direction": "S"},
        },
    },
    # Sensor 3 data format
    [
        ("city", "Zaporizhzhia"),
        ("temp_celsius", 9.3),
        ("humidity_percent", 79),
        ("wind_mps", 5.0),
    ],
    [
        ("city", "Mykolaiv"),
        ("temp_celsius", 14.2),
        ("humidity_percent", 68),
        ("wind_mps", 6.2),
    ],
]


def get_raw_data():
    return random.choice(_MOCK_DATA)


if __name__ == "__main__":
    for call_number in range(5):
        print(f"Call #{call_number + 1}:")
        raw_data = get_raw_data()
        print(f"  Data type: {type(raw_data)}")
        print(f"  Received data: {raw_data}\n")
