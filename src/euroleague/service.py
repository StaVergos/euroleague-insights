from src.euroleague.api import EuroleagueAPI
from src.euroleague.schemas.clubs import ClubResponse


class EuroleagueService:
    def __init__(self, api: EuroleagueAPI) -> None:
        self.api = api

    async def get_clubs(self) -> ClubResponse:
        club_response = await self.api.get_clubs()
        return club_response
