from __future__ import annotations

from turtle import end_fill

from fastapi_gql.infra.database import engine, meta
from fastapi_gql.models.user import users

meta.create_all(engine)
