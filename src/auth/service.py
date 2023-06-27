from sqlalchemy.orm import Session

from auth.models import User
from auth.schemas import UserCreate


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 20):
    return db.query(User).offset(skip).limit(limit).all()


def create_user(db: Session, user: UserCreate, role: int = 4):
    db_user = User(email=user.email, role=role)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
