from app.domain.entities.health import HealthStatus
from app.infrastructure.repositories.system_repository import SystemRepository


class GetHealthUseCase:
    def __init__(self, repository: SystemRepository) -> None:
        self._repository = repository

    def execute(self) -> HealthStatus:
        return self._repository.get_health_status()
