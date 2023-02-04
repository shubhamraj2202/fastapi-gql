from __future__ import annotations

from fastapi import FastAPI

from fastapi_gql.controllers.index import user

app = FastAPI()
app.include_router(user)
