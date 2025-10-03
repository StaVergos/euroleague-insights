import httpx
from fastapi import Depends, Request
from src.db.postgresql import get_db as get_database

from src.euroleague.api import EuroleagueAPI
from src.euroleague.service import EuroleagueService
from src.insights.service import InsightsService


def get_http_client(request: Request) -> httpx.AsyncClient:
    return request.app.state.http


def get_euroleague_api(
    client: httpx.AsyncClient = Depends(get_http_client),
) -> EuroleagueAPI:
    return EuroleagueAPI(client=client)


def get_db():
    yield from get_database()


def get_euroleague_service(
    api: EuroleagueAPI = Depends(get_euroleague_api),
) -> EuroleagueService:
    return EuroleagueService(api=api)


def get_insights_service(
    euroleague_service: EuroleagueService = Depends(get_euroleague_service),
    db=Depends(get_database),
) -> InsightsService:
    return InsightsService(euroleague_service=euroleague_service, db=db)
