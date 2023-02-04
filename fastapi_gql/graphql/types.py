from __future__ import annotations

from typing import List

import strawberry
from strawberry.types import Info

from fastapi_gql.infra.database import conn
from fastapi_gql.models.index import users


@strawberry.type
class User:
    id: int
    name: str
    email: str
    password: str


@strawberry.type
class Query:
    @strawberry.field
    def user(self, id: int) -> User:
        return conn.execute(users.select().where(users.c.id == id)).fetchone()

    @strawberry.field
    def users(self) -> List[User]:
        return conn.execute(users.select()).fetchall()


@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_flavour(self, name: str, info: Info) -> bool:
        return True

    @strawberry.mutation
    async def create_user(
        self,
        name: str,
        email: str,
        password: str,
        info: Info,
    ) -> int:
        user = {"name": name, "email": email, "password": password}
        result = conn.execute(users.insert(), user)
        return int(result.inserted_primary_key[0])

    @strawberry.mutation
    def update_user(
        self,
        id: int,
        name: str,
        email: str,
        password: str,
        info: Info,
    ) -> str:
        result = conn.execute(
            users.update().where(users.c.id == id),
            {"name": name, "email": email, "password": password},
        )
        print(result.returns_rows)
        return str(result.rowcount) + " Row(s) updated"

    @strawberry.mutation
    def delete_user(self, id: int) -> bool:
        result = conn.execute(users.delete().where(users.c.id == id))
        return result.rowcount > 0
