from pydantic import BaseModel


class HealthResponse(BaseModel):
    status: str


class InfoResponse(BaseModel):
    name: str
    version: str
    description: str
    environment: str


class WeatherResponse(BaseModel):
    city: str
    country: str
    temperature_c: float
    wind_speed_kmh: float
    weather_code: int
    observed_at: str


class CountryEconomyResponse(BaseModel):
    country: str
    country_code: str
    year: int
    gdp_billion_usd: float
    population_million: float
    inflation_rate: float
