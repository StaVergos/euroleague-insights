from fastapi import FastAPI, Depends

from src.euroleague.schemas.clubs import DTOClub
from src.euroleague.service import EuroleagueService

app = FastAPI()


@app.get("/health")
def healthcheck():
    return {"status": "ok"}


@app.get("/")
def main():
    return "Hello World"


@app.get("/clubs")
def get_clubs(euroleague_service=Depends(EuroleagueService)) -> list[DTOClub]:
    return euroleague_service.get_clubs()
