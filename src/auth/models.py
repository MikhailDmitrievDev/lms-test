import enum
from typing import Optional

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum, Text
from sqlalchemy.orm import relationship

from database import Base


class Role(enum.Enum):
    admin = 1
    moderator = 2
    teacher = 3
    student = 4


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), unique=True, index=True, nullable=False)
    role = Column(Enum(Role))

    profile = relationship("Profile", back_populates="owner", uselist=False)


class Profile(Base):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), unique=True, index=True, nullable=False)
    first_name = Column(Optional[String(50)], nullable=False)
    middle_name = Column(Optional[String(50)], nullable=True, )
    last_name = Column(Optional[String(50)], nullable=False)
    bio = Column(Text, nullable=False)
    is_active = Column(Boolean, default=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)

    owner = relationship("User", back_populates="profile")
