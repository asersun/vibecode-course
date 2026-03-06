from dataclasses import dataclass


@dataclass(frozen=True)
class CountryEconomy:
    country: str
    country_code: str
    year: int
    gdp_usd: float
    population: int
    inflation_rate: float
