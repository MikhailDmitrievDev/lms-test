from fastapi import APIRouter, Depends

router = APIRouter()


@router.get("/users")
def view_users():
    return {"name": "Vasya"}