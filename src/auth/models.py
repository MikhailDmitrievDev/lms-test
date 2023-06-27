import enum

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum, Text
from sqlalchemy.orm import relationship

from mixins import Timestamp
from database import Base


class Role(enum.Enum):
    admin = 1
    moderator = 2
    teacher = 3
    student = 4


class User(Base, Timestamp):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), unique=True, index=True, nullable=False)
    role = Column(Enum(Role))

    profile = relationship("Profile", back_populates="owner", uselist=False)


class Profile(Base, Timestamp):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50), nullable=False)
    middle_name = Column(String(50), nullable=True)
    last_name = Column(String(50), nullable=False)
    bio = Column(Text, nullable=True)
    is_active = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    owner = relationship("User", back_populates="profile")
