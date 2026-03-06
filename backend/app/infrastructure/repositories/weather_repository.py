import json
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import urlopen

from app.domain.entities.weather import CurrentWeather


class WeatherRepository:
    _GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
    _FORECAST_URL = "https://api.open-meteo.com/v1/forecast"

    def get_current_weather_by_city(self, city: str) -> CurrentWeather:
        geo_payload = self._fetch_json(
            self._GEOCODING_URL,
            {
                "name": city,
                "count": 1,
                "language": "en",
                "format": "json",
            },
        )

        results = geo_payload.get("results") or []
        if not results:
            raise ValueError(f"City '{city}' was not found")

        location = results[0]
        latitude = location["latitude"]
        longitude = location["longitude"]

        weather_payload = self._fetch_json(
            self._FORECAST_URL,
            {
                "latitude": latitude,
                "longitude": longitude,
                "current": "temperature_2m,weather_code,wind_speed_10m",
                "timezone": "auto",
            },
        )

        current = weather_payload.get("current")
        if not current:
            raise RuntimeError("Weather provider did not return current weather data")

        return CurrentWeather(
            city=location.get("name", city),
            country=location.get("country", "Unknown"),
            temperature_c=float(current["temperature_2m"]),
            wind_speed_kmh=float(current["wind_speed_10m"]),
            weather_code=int(current["weather_code"]),
            observed_at=str(current["time"]),
        )

    def _fetch_json(self, base_url: str, params: dict[str, object]) -> dict:
        url = f"{base_url}?{urlencode(params)}"
        try:
            with urlopen(url, timeout=10) as response:
                return json.loads(response.read().decode("utf-8"))
        except (HTTPError, URLError) as exc:
            raise RuntimeError("Unable to fetch weather data from provider") from exc
