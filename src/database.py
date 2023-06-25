from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from var_env import POSTGRES_USER, \
    POSTGRES_DB, \
    POSTGRES_PORT, \
    POSTGRES_HOST, \
    POSTGRES_PASSWORD

SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg2://{POSTGRES_USER}:" \
                          f"{POSTGRES_PASSWORD}@" \
                          f"{POSTGRES_HOST}:" \
                          f"{POSTGRES_PORT}/" \
                          f"{POSTGRES_DB}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={}, future=True
)

SessionLocal = sessionmaker(autocommit=False,
                            autoflush=False,
                            bind=engine,
                            future=True)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
