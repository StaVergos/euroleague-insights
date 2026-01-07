import httpx

from euroleague_insights.euroleague.euroleague_api.constants import CompetitionCode
from euroleague_insights.euroleague.euroleague_api.constants import EuroleagueApiUrl
from euroleague_insights.euroleague.euroleague_api.constants import EuroleagueLive
from euroleague_insights.euroleague.euroleague_api.constants import SeasonCode
from euroleague_insights.euroleague.models import Match


class EuroleagueAPI:
    def __init__(self, season: str):
        self.season = SeasonCode(season)
        self.client = httpx.Client()
        self.live_client = httpx.Client()

    @property
    def api_v2(self) -> str:
        return EuroleagueApiUrl.V2.value

    @property
    def live_api(self) -> str:
        return EuroleagueLive.value

    def euroleague_2024_games_url(self) -> str:
        return (
            f"{self.api_v2}"
            f"/competitions/{CompetitionCode.EUROLEAGUE.value}"
            f"/seasons/{self.season.value}/games"
        )

    def euroleague_clubs_url(self) -> str:
        return (
            f"{self.api_v2}"
            f"/competitions/{CompetitionCode.EUROLEAGUE.value}"
            f"/seasons/{self.season.value}/clubs"
        )

    def euroleague_players_url(self) -> str:
        return (
            f"{self.api_v2}"
            f"/competitions/{CompetitionCode.EUROLEAGUE.value}"
            f"/seasons/{self.season.value}/people"
        )

    def euroleague_matches_url(self) -> str:
        return (
            f"{self.api_v2}"
            f"/competitions/{CompetitionCode.EUROLEAGUE.value}"
            f"/seasons/{self.season.value}/games"
        )

    def euroleague_plays_url(self) -> str:
        return (
            f"{self.live_api}/PlaybyPlay"
            f"?gamecode={Match.game_code}"
            f"&seasoncode={self.season.value}"
        )

    def get_clubs(self):
        response = self.client.get(self.euroleague_clubs_url())
        response.raise_for_status()
        return response.json()

    def get_players(self):
        response = self.client.get(self.euroleague_players_url())
        response.raise_for_status()
        return response.json()

    def get_matches(self):
        response = self.client.get(self.euroleague_matches_url())
        response.raise_for_status()
        return response.json()

    def get_plays(self):
        response = self.client.get(self.euroleague_plays_url())
        response.raise_for_status()
        return response.json()
