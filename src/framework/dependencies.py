import httpx
from fastapi import Depends, Request

from src.euroleague.api import EuroleagueAPI
from src.euroleague.service import EuroleagueService


def get_http_client(request: Request) -> httpx.AsyncClient:
    return request.app.state.http


def get_euroleague_api(
    client: httpx.AsyncClient = Depends(get_http_client),
) -> EuroleagueAPI:
    return EuroleagueAPI(client=client)


def get_euroleague_service(
    api: EuroleagueAPI = Depends(get_euroleague_api),
) -> EuroleagueService:
    return EuroleagueService(api=api)
