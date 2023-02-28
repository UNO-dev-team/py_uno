from fastapi import FastAPI, APIRouter
from src.controllers import user


def add_routes(app: FastAPI) -> None:
    api_router = APIRouter(
        prefix='/api'
    )
    api_router.include_router(user.router)
    app.include_router(api_router)
