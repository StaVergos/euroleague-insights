from contextlib import asynccontextmanager

import httpx
from fastapi import Depends, FastAPI

from src.euroleague.schemas.clubs import DTOClub
from src.framework.dependencies import get_euroleague_service


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.http = httpx.AsyncClient(timeout=10)
    try:
        yield
    finally:
        await app.state.http.aclose()


app = FastAPI(lifespan=lifespan)


@app.get("/health")
def healthcheck():
    return {"status": "ok"}


@app.get("/")
def main():
    return "Hello World"


@app.get("/clubs", response_model=list[DTOClub])
async def get_clubs(service=Depends(get_euroleague_service)):
    return await service.get_clubs()
