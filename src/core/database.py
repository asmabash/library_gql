from sqlalchemy.orm import sessionmaker
from src.models.base import Base
from src.core.config import DATABASE_URL
from sqlalchemy import create_engine


engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(
    bind=engine,
    expire_on_commit=False
)

# create db tables
def init_db():
    Base.metadata.create_all(bind=engine)
