from fastapi import APIRouter, HTTPException, Query

from app.application.use_cases.get_country_economy import GetCountryEconomyUseCase
from app.application.use_cases.get_health import GetHealthUseCase
from app.application.use_cases.get_info import GetInfoUseCase
from app.application.use_cases.get_weather import GetWeatherUseCase
from app.infrastructure.repositories.country_economy_repository import CountryEconomyRepository
from app.infrastructure.repositories.system_repository import SystemRepository
from app.infrastructure.repositories.weather_repository import WeatherRepository
from app.presentation.api.schemas import (
    CountryEconomyResponse,
    HealthResponse,
    InfoResponse,
    WeatherResponse,
)

router = APIRouter(prefix="/api", tags=["system"])

_repository = SystemRepository()
_get_health_use_case = GetHealthUseCase(repository=_repository)
_get_info_use_case = GetInfoUseCase(repository=_repository)
_weather_repository = WeatherRepository()
_get_weather_use_case = GetWeatherUseCase(repository=_weather_repository)
_country_economy_repository = CountryEconomyRepository()
_get_country_economy_use_case = GetCountryEconomyUseCase(repository=_country_economy_repository)


@router.get("/health", response_model=HealthResponse, summary="Health check")
def health() -> HealthResponse:
    result = _get_health_use_case.execute()
    return HealthResponse(status=result.status)


@router.get("/info", response_model=InfoResponse, summary="Application information")
def get_info() -> InfoResponse:
    result = _get_info_use_case.execute()
    return InfoResponse(
        name=result.name,
        version=result.version,
        description=result.description,
        environment=result.environment,
    )


@router.get("/weather", response_model=WeatherResponse, summary="Current weather by city")
def get_weather(city: str = Query(..., min_length=2, description="City name")) -> WeatherResponse:
    try:
        result = _get_weather_use_case.execute(city=city)
        return WeatherResponse(
            city=result.city,
            country=result.country,
            temperature_c=result.temperature_c,
            wind_speed_kmh=result.wind_speed_kmh,
            weather_code=result.weather_code,
            observed_at=result.observed_at,
        )
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    except RuntimeError as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc


@router.get(
    "/country-economy",
    response_model=CountryEconomyResponse,
    summary="Country GDP, population and inflation",
)
def get_country_economy(
    country: str = Query(..., min_length=2, description="Country name or ISO code"),
) -> CountryEconomyResponse:
    try:
        result = _get_country_economy_use_case.execute(country=country)
        return CountryEconomyResponse(
            country=result.country,
            country_code=result.country_code,
            year=result.year,
            gdp_billion_usd=round(result.gdp_usd / 1_000_000_000, 2),
            population_million=round(result.population / 1_000_000, 2),
            inflation_rate=round(result.inflation_rate, 2),
        )
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    except RuntimeError as exc:
        raise HTTPException(status_code=502, detail=str(exc)) from exc
