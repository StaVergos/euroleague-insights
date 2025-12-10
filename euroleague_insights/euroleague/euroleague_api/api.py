import httpx

from euroleague_insights.euroleague.euroleague_api.constants import CompetitionCode
from euroleague_insights.euroleague.euroleague_api.constants import EuroleagueApiUrl
from euroleague_insights.euroleague.euroleague_api.constants import SeasonCode


class EuroleagueAPI:
    def __init__(self):
        self.client = httpx.Client()
        self.live_client = httpx.Client()

    @property
    def api_v2(self) -> str:
        return EuroleagueApiUrl.V2.value

    def euroleague_2024_games_url(self, season_code: SeasonCode) -> str:
        return (
            f"{self.api_v2}"
            f"/competitions/{CompetitionCode.EUROLEAGUE.value}"
            f"/seasons/{season_code.value}/games"
        )

    def euroleague_clubs_url(self, season_code: SeasonCode) -> str:
        return (
            f"{self.api_v2}"
            f"/competitions/{CompetitionCode.EUROLEAGUE.value}"
            f"/seasons/{season_code.value}/clubs"
        )

    def get_clubs(self, season: SeasonCode):
        response = self.client.get(self.euroleague_clubs_url(season))
        response.raise_for_status()
        return response.json()
