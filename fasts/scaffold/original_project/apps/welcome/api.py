
from fastapi import APIRouter

router = APIRouter()


@router.get("/", name="welcome")
def welcome():
    return {"message": "Hello from welcome!"}


__all__ = ['router']
