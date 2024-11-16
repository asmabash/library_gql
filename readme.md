# Library System using GraphQL and SQLAlchemy


## Installation

To run the project in your local environment:

  1. Create and activate a virtual environment:
```
  $ python -m venv virtualenv
  $ source env/bin/activate
```
  2. Install requirements:
```
  $ pip install -r requirements.txt
```
  3. Run the application:
```
  $ strawberry server schema
```

GraphQL server should now be available at http://localhost:8000/graphql

## Example usage
To get all authors, we can run the following query:

```gql
query GetAuthors {
  authors {
    name
  }
}
```

We would get this response from GQL:

```gql
{
  "data": {
    "authors": [
      {
        "name": "Clive Thompson"
      },
      {
        "name": "Eric Evans"
      }
    ]
  }
}
```
