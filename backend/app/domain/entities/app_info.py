from dataclasses import dataclass


@dataclass(frozen=True)
class AppInfo:
    name: str
    version: str
    description: str
    environment: str
