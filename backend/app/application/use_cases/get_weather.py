from app.domain.entities.weather import CurrentWeather
from app.infrastructure.repositories.weather_repository import WeatherRepository


class GetWeatherUseCase:
    def __init__(self, repository: WeatherRepository) -> None:
        self._repository = repository

    def execute(self, city: str) -> CurrentWeather:
        return self._repository.get_current_weather_by_city(city=city)
