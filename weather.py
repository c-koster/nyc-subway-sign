from dataclasses import dataclass
import requests

BASE_URL = "https://api.open-meteo.com"


@dataclass(frozen=True)
class WeatherForecast:
    high_temp: float
    low_temp: float
    precipitation_probability: float


def get_weather_data(lat=40.71517, long=-73.94145, forecast_days=1):
    params = {
        "latitude": lat,
        "longitude": long,
        "daily": "temperature_2m_max,temperature_2m_min,precipitation_probability_max",
        "timezone": "America/New_York",
        "temperature_unit": "fahrenheit",
        "forecast_days": forecast_days,
    }

    response = requests.get("https://api.open-meteo.com/v1/forecast", params=params)

    data = response.json()

    daily_weather = data["daily"]
    weather_data = dict()

    # Iterate through the keys in the original data
    for key, value in daily_weather.items():
        weather_data[key] = value[0]

    forecast_instance = WeatherForecast(
        high_temp=weather_data["temperature_2m_max"],
        low_temp=weather_data["temperature_2m_min"],
        precipitation_probability=weather_data["precipitation_probability_max"],
    )

    return forecast_instance


if __name__ == "__main__":
    print(get_weather_data())
