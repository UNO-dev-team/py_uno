from fastapi import FastAPI
from src.routes.router import add_routes

app = FastAPI()
add_routes(app)
