from fastapi.routing import APIRouter
from fastapi import Body, Path, Query
from typing import Optional
from src.models.user import User


router = APIRouter(
    prefix="/user"
)

@router.post("/")
def create_user(user: User = Body(...)):
    user.do_something()
    return user


@router.get("/")
def get_user(
        uuid: int = Query(...),
        name: Optional[str] = Query(None, min_length=1, max_length=100)
    ):

    return {
        "id": uuid,
        "name": name
    }


@router.get("/{uuid}")
def show_user(uuid: int = Path(...)):
    return {
        "uuid": uuid,
        "msg": "It exists!"
    }


