import sqlalchemy
from .base import metadata

users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("phone", sqlalchemy.String),
    sqlalchemy.Column("email", sqlalchemy.String, unique=True),
    sqlalchemy.Column("comment", sqlalchemy.String),
)
