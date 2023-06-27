from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from auth.schemas import User
from auth.service import get_user, \
    get_user_by_email, \
    get_users, \
    create_user
from database import get_db

router = APIRouter()


@router.get("/users", response_model=List[User])
async def view_get_users(skip: int = 0, limit: int = 20, db: Session = Depends(get_db)):
    users = get_users(db, skip=skip, limit=limit)
    return users
