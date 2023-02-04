from __future__ import annotations

from sqlalchemy import Column, Integer, String, Table
from sqlalchemy.sql.sqltypes import Integer, String

from fastapi_gql.infra.database import meta

users = Table(
    "users",
    meta,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(length=255)),
    Column("email", String(length=255)),
    Column("password", String(length=255)),
)
