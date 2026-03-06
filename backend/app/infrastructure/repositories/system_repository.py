from app.domain.entities.app_info import AppInfo
from app.domain.entities.health import HealthStatus


class SystemRepository:
    """Infrastructure source for system-level data.

    Data is intentionally hardcoded for now.
    """

    def get_health_status(self) -> HealthStatus:
        return HealthStatus(status="ok")

    def get_app_info(self) -> AppInfo:
        return AppInfo(
            name="backend",
            version="1.0.0",
            description="edited page info FastAPI backend following clean architecture",
            environment="development",
        )
