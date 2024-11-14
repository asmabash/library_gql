from __future__ import annotations
from typing import Optional
import strawberry

@strawberry.type
class Book:
    title: str
    author: Optional[Author] = strawberry.field(default_factory=list)

@strawberry.type
class Author:
    name: str
    books: Optional[list[Book]] = strawberry.field(default_factory=list)
