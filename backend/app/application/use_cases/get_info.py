from app.domain.entities.app_info import AppInfo
from app.infrastructure.repositories.system_repository import SystemRepository


class GetInfoUseCase:
    def __init__(self, repository: SystemRepository) -> None:
        self._repository = repository

    def execute(self) -> AppInfo:
        return self._repository.get_app_info()
