from fastapi import FastAPI

from app.presentation.api.routes.system import router as system_router

app = FastAPI(
    title="Backend API",
    version="1.0.0",
    description="Clean architecture FastAPI backend",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.include_router(system_router)
