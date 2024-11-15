from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import String

from src.models.base import Base

class Book(Base):
    # alternatively, we can have a method in Base class to
    # automatically generate all table names
    __tablename__ = "book"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(30))
    genre: Mapped[str] = mapped_column(String(30))
    author_id: Mapped[int] = mapped_column()
