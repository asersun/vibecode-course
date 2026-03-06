import json
import time
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import urlopen

from app.domain.entities.country_economy import CountryEconomy


class CountryEconomyRepository:
    _WORLD_BANK_BASE_URL = "https://api.worldbank.org/v2"
    _GDP_INDICATOR = "NY.GDP.MKTP.CD"
    _POPULATION_INDICATOR = "SP.POP.TOTL"
    _INFLATION_INDICATOR = "FP.CPI.TOTL.ZG"

    def get_country_economy(self, country: str) -> CountryEconomy:
        country_code, country_name = self._resolve_country(country)

        gdp_by_year = self._get_indicator_series(country_code, self._GDP_INDICATOR)
        population_by_year = self._get_indicator_series(country_code, self._POPULATION_INDICATOR)
        inflation_by_year = self._get_indicator_series(country_code, self._INFLATION_INDICATOR)

        common_years = set(gdp_by_year) & set(population_by_year) & set(inflation_by_year)
        if not common_years:
            raise RuntimeError("No complete economy dataset available for this country")

        latest_year = max(common_years)

        return CountryEconomy(
            country=country_name,
            country_code=country_code,
            year=latest_year,
            gdp_usd=float(gdp_by_year[latest_year]),
            population=int(population_by_year[latest_year]),
            inflation_rate=float(inflation_by_year[latest_year]),
        )

    def _resolve_country(self, country_query: str) -> tuple[str, str]:
        payload = self._fetch_world_bank_json(
            "/country",
            {"format": "json", "per_page": 400},
        )
        countries = payload[1] if isinstance(payload, list) and len(payload) > 1 else []

        normalized_query = country_query.strip().lower()
        partial_matches: list[tuple[str, str]] = []
        for country in countries:
            name = str(country.get("name", "")).strip()
            iso2_code = str(country.get("iso2Code", "")).strip()
            country_id = str(country.get("id", "")).strip()
            region = country.get("region", {}) or {}
            if region.get("id") == "NA":
                continue
            if (
                name.lower() == normalized_query
                or iso2_code.lower() == normalized_query
                or country_id.lower() == normalized_query
            ):
                return country_id, name
            if normalized_query in name.lower():
                partial_matches.append((country_id, name))

        if partial_matches:
            return partial_matches[0]

        raise ValueError(f"Country '{country_query}' was not found")

    def _get_indicator_series(self, country_code: str, indicator: str) -> dict[int, float]:
        payload = self._fetch_world_bank_json(
            f"/country/{country_code}/indicator/{indicator}",
            {"format": "json", "per_page": 70},
        )
        records = payload[1] if isinstance(payload, list) and len(payload) > 1 else []
        series: dict[int, float] = {}
        for row in records:
            value = row.get("value")
            date = row.get("date")
            if value is None or date is None:
                continue
            year = int(date)
            series[year] = float(value)
        return series

    def _fetch_world_bank_json(self, path: str, params: dict[str, object]) -> object:
        url = f"{self._WORLD_BANK_BASE_URL}{path}?{urlencode(params)}"
        for attempt in range(2):
            try:
                with urlopen(url, timeout=20) as response:
                    return json.loads(response.read().decode("utf-8"))
            except (HTTPError, URLError, TimeoutError):
                if attempt == 0:
                    time.sleep(0.5)
                    continue
                raise RuntimeError("Unable to fetch economy data from provider")
