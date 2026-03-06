from app.domain.entities.country_economy import CountryEconomy
from app.infrastructure.repositories.country_economy_repository import CountryEconomyRepository


class GetCountryEconomyUseCase:
    def __init__(self, repository: CountryEconomyRepository) -> None:
        self._repository = repository

    def execute(self, country: str) -> CountryEconomy:
        return self._repository.get_country_economy(country=country)
