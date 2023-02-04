from __future__ import annotations

import strawberry
from fastapi import APIRouter
from strawberry.asgi import GraphQL

from fastapi_gql.graphql.types import Mutation, Query
from fastapi_gql.infra.database import conn
from fastapi_gql.models.index import users

user = APIRouter()
schema = strawberry.Schema(Query, Mutation)
graphql_app = GraphQL(schema)
user.add_route("/graphql", graphql_app)
