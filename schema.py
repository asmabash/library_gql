from src.crud.author import create_author, get_authors
from src.core.database import init_db
import strawberry

from src.scalars import AddAuthorInput, Author, Book


@strawberry.type
class Query:
    @strawberry.field
    def get_author_for_book(root) -> "Author":
        author = Author(name="Michael Crichton")
        book1 = Book(title="Coders", author=author)
        book2 = Book(title="Sphere", author=author)
        author.books = [book1, book2]
        return author

    @strawberry.field
    def books(root) -> list[Book]:
        author1 = Author(name="Michael Crichton")
        author2 = Author(name="Sheryl Sandberg")
        book1 = Book(title="Coders", author=author1)
        book2 = Book(title="Sphere", author=author1)
        book3 = Book(title="Option B", author=author2)
        return [book1, book2, book3]

    @strawberry.field
    def authors(root) -> list[Author]:
        authors = get_authors()
        return authors

@strawberry.type
class Mutation:
    @strawberry.field
    def add_author(self, author: AddAuthorInput) -> Author:
        author = create_author(author.name)
        return author

init_db()
schema = strawberry.Schema(query=Query, mutation=Mutation)
