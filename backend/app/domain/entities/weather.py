from dataclasses import dataclass


@dataclass(frozen=True)
class CurrentWeather:
    city: str
    country: str
    temperature_c: float
    wind_speed_kmh: float
    weather_code: int
    observed_at: str
