
from sqlalchemy import select, insert
from src.models.author import Author
from src.core.database import SessionLocal

def get_authors():
    # TODO: return their books as well
    with SessionLocal() as session:
        query = select(Author)
        result = (session.scalars(query)).all()
        return result

def create_author(name) -> Author:
    with SessionLocal() as session:
        query = insert(Author).values(name=name).returning(Author)
        result = (session.execute(query)).scalar()
        session.commit()
        return result
